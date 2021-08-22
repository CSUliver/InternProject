<template>
  <div class="app-container">
    <!-- 模板 -->
    <!-- 1.搜索栏 -->
    <div id="search">
      <!-- {{params}} -->
      <el-input
        style="width: 300px; margin-right: 10px"
        placeholder="请输入关键字"
        v-model="params.search"
        clearable
      >
      </el-input>
      <el-select
        style="margin-right: 10px"
        v-model="params.is_active"
        clearable
        placeholder="请选择用户状态"
      >
        <el-option label="冻结" value="0"></el-option>
        <el-option label="活跃" value="1"></el-option>
      </el-select>
      <el-select
        v-model="params.is_superuser"
        clearable
        placeholder="请选择用户类型"
      >
        <el-option label="超级管理员" value="1"></el-option>
        <el-option label="普通用户" value="0"></el-option>
      </el-select>
      <el-button
        type="primary"
        plain
        style="float: right"
        @click="addUserFormVisible = true;adduserform={}"
        >新增用户</el-button
      >
    </div>

    <!-- 2.数据展示表格 -->
    <div id="datatable">
      <el-table border :data="tableData" style="width: 100%; margin-top: 15px">
        <el-table-column label="编号" width="80">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.$index + 1 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="用户账号">
          <template slot-scope="scope">
            <el-popover trigger="hover" placement="top">
              <p>姓名: {{ scope.row.first_name }}-{{ scope.row.last_name }}</p>
              <div slot="reference" class="name-wrapper">
                <el-tag size="medium">{{ scope.row.username }}</el-tag>
              </div>
            </el-popover>
          </template>
        </el-table-column>
        <el-table-column label="用户头像">
          <template slot-scope="scope">
            <el-image
              style="width: 40px; height: 40px"
              :src="scope.row.avatar"
            ></el-image>
          </template>
        </el-table-column>
        <el-table-column label="电话">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.row.tel }}</span>
          </template>
        </el-table-column>
        <el-table-column label="管理员权限">
          <template slot-scope="scope">
            <!-- <el-tooltip :content="scope.row.is_superuser ? '机场管理员' : '其他用户'"
              placement="top"> -->
            <el-tooltip v-if="scope.row.person_type==='admin'" :content="机场管理员" 
              placement="top">
              <el-switch
                v-model="scope.row.person_type"
                active-color="#13ce66"
                inactive-color="#ff4949"
                active-value="admin"
                inactive-value=""
                disabled
              >
              </el-switch>
            </el-tooltip>
            <el-tooltip v-if="scope.row.person_type!=='admin'" :content="其他用户" 
              placement="top">
              <el-switch
                v-model="deftrue"
                active-color="#ff4949"
                inactive-color="#13ce66"
                active-value="1"
                inactive-value="0"
                disabled
              >
              </el-switch>
            </el-tooltip>
          </template>
        </el-table-column>
        <el-table-column label="用户状态">
          <template slot-scope="scope">
            <el-tag v-if="scope.row.is_active" type="success">活跃</el-tag>
            <el-tag v-else type="info">冻结</el-tag>
            <!-- <span style="margin-left: 10px">{{ scope.row.is_active }}</span> -->
          </template>
        </el-table-column>
        <el-table-column label="注册时间" width="240px">
          <template slot-scope="scope">
            <i class="el-icon-time"></i>
            <span style="margin-left: 10px">{{ scope.row.date_joined }}</span>
          </template>
        </el-table-column>
        <el-table-column label="用户类别">
          <template slot-scope="scope">
            
            <el-tag v-if="scope.row.person_type==='admin'" type="success">机场管理员</el-tag>
            <el-tag v-else-if="scope.row.person_type==='passenger'">旅客</el-tag>
            <el-tag v-else-if="scope.row.person_type==='flight'" type="info">机组人员</el-tag>
            <el-tag v-else-if="scope.row.person_type==='airport'" type="warning">机场工作人员</el-tag>
            <span v-else>{{ scope.row.person_type }}</span>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)"
              >编辑</el-button
            >
            <el-button
              size="mini"
              type="danger"
              @click="handleDelete(scope.row.id)"
              >删除</el-button
            >
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!-- 3.分页 -->
    <div id="pagenations">
      <el-pagination
        style="float: right; margin-top: 15px"
        background
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="params.page"
        :page-sizes="[5, 10, 15, 20]"
        :page-size="params.page_size"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total_number"
      >
      </el-pagination>
    </div>
    <!-- 新增用户模态框 -->
    <el-dialog title="新增用户" :visible.sync="addUserFormVisible">
      {{adduserform}}
      <el-form :model="adduserform">
        <el-form-item label="用户账号" :label-width="formLabelWidth">
          <el-input
            v-model="adduserform.username"
            autocomplete="off"
          ></el-input>
        </el-form-item>

        <el-form-item label="用户密码" :label-width="formLabelWidth">
          <el-input
            v-model="adduserform.password"
            autocomplete="off"
            show-password
          ></el-input>
        </el-form-item>

        <el-form-item label="用户姓氏" :label-width="formLabelWidth">
          <el-input
            v-model="adduserform.first_name"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="用户名字" :label-width="formLabelWidth">
          <el-input
            v-model="adduserform.last_name"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="用户邮箱" :label-width="formLabelWidth">
          <el-input v-model="adduserform.email" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="联系方式" :label-width="formLabelWidth">
          <el-input v-model="adduserform.tel" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="微信" :label-width="formLabelWidth">
          <el-input v-model="adduserform.wechat" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="用户类型" :label-width="formLabelWidth">
          <el-radio-group v-model="adduserform.is_superuser" size="medium">
            <el-radio border label="1">超级管理员</el-radio>
            <el-radio border label="0">普通用户</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="用户活跃状态" :label-width="formLabelWidth">
          <el-select v-model="adduserform.is_active" placeholder="请选择用户状态">
            <el-option label="活跃" value="1"></el-option>
            <el-option label="冻结" value="0"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="用户类型" :label-width="formLabelWidth">
          <el-radio-group v-model="adduserform.person_type" size="medium">
            <el-radio border label="admin">机场管理员</el-radio>
            <el-radio border label="passenger">旅客</el-radio>
            <el-radio border label="airport">机场工作人员</el-radio>
            <el-radio border label="flight">机组人员</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="用户头像" :label-width="formLabelWidth">
          <el-upload
            class="avatar-uploader"
            action="11"
            :auto-upload="false"
            :show-file-list="false"
            :on-change="handlefileChange"
            :before-upload="beforeAvatarUpload"
          >
            <img v-if="imageUrl" :src="imageUrl" class="avatar" />
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item> 
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="addUserFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="addUserInfo"
          >确 定</el-button
        >
      </div>
    </el-dialog>

    <!-- 编辑用户模态框 -->
    <el-dialog title="编辑用户" :visible.sync="editUserFormVisible">
      <!-- {{edituserform}} -->
      <el-form :model="edituserform">
        <el-form-item label="用户账号" :label-width="formLabelWidth">
          <el-input
            v-model="edituserform.username"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="用户密码" :label-width="formLabelWidth">
          <el-input type="password" show-password
            v-model="edituserform.password"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="用户姓氏" :label-width="formLabelWidth">
          <el-input
            v-model="edituserform.first_name"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="用户名字" :label-width="formLabelWidth">
          <el-input
            v-model="edituserform.last_name"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="用户邮箱" :label-width="formLabelWidth">
          <el-input v-model="edituserform.email" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="联系方式" :label-width="formLabelWidth">
          <el-input v-model="edituserform.tel" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="微信" :label-width="formLabelWidth">
          <el-input v-model="edituserform.wechat" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="用户类型" :label-width="formLabelWidth">
          <el-radio-group v-model="edituserform.is_superuser" size="medium">
            <el-radio border label="1">超级管理员</el-radio>
            <el-radio border label="0">普通用户</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="用户类型" :label-width="formLabelWidth">
          <el-radio-group v-model="edituserform.person_type" size="medium">
            <el-radio border label="admin">机场管理员</el-radio>
            <el-radio border label="passenger">旅客</el-radio>
            <el-radio border label="airport">机场工作人员</el-radio>
            <el-radio border label="flight">机组人员</el-radio>
          </el-radio-group>
        </el-form-item>
        <!-- <el-form-item label="用户状态" :label-width="formLabelWidth">
          <el-radio-group v-model="adduserform.is_superuser" size="medium">
            <el-radio border label="活跃"></el-radio>
            <el-radio border label="冻结"></el-radio>
          </el-radio-group>
        </el-form-item> -->
        <el-form-item label="用户活跃状态" :label-width="formLabelWidth">
          <el-select v-model="edituserform.is_active" placeholder="请选择用户状态">
            <el-option label="活跃" value="1"></el-option>
            <el-option label="冻结" value="0"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="用户管理状态" :label-width="formLabelWidth">
          <el-select v-model="edituserform.is_staff" placeholder="请选择用户状态">
            <el-option label="管理者" value="1"></el-option>
            <el-option label="非管理者" value="0"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="用户头像" :label-width="formLabelWidth">
          <el-upload
            class="avatar-uploader"
            action="11"
            :auto-upload="false"
            :show-file-list="false"
            :on-change="handlefileChange"
            :before-upload="beforeAvatarUpload"
          >
            <img v-if="imageUrl" :src="imageUrl" class="avatar" />
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="editUserFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="editUserInfo"
          >确 定</el-button
        >
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { Form } from 'element-ui';
import request from "../../../utils/request.js";
export default {
  data() {
    return {
      // 所有的数据变量定义在此处
      value: "",
      deftrue: true,
      input: "",
      // 表格数据
      tableData: [],
      // 获取用户数据的参数
      params: {
        page: 1, // 默认显示第一页
        page_size: 5, // 默认每页显示的条数
      },
      total_number: 0, // 数据总条数
      // 新增用户表单数据
      addUserFormVisible: false,
      editUserFormVisible: false,
      formLabelWidth: "120px",
      adduserform: {},
      // 编辑用户表单数据
      edituserform:{},
      
      imageUrl:''
    };
  },
  // 初始化完成:data中的数据以及methods中的方法均可使用
  created() {
    this.fetchUserData();
  },
  // 侦听器-监听器
  watch: {
    params: {
      handler: function (newparams, oldparams) {
        //时刻监听params数据的变化，一旦发生变化自动调用该方法
        console.log(newparams, oldparams);
        // 重新加载数据
        this.fetchUserData();
      },
      deep: true, // 深度监听（对象或数据）
    },
  },
  methods: {
    // 新增用户信息
    addUserInfo:function(){
      // 发起请求：新增用户-如果不涉及图片
      // request({url:"/users/users/",method:"post",data:this.adduserform}).then(res=>{
      //   // 请求成功后的逻辑处理
      // })
      // 发起请求：新增用户-涉及到文件上传（二进制流）
      /*
        FormData:用键值对模拟表单控件，用form表单控件中的name以及value值组成一个querystring
        作用：一般用来异步上传二进制文件
      */
      var addform = new FormData()
      addform.append('username',this.adduserform.username)
      addform.append('password',this.adduserform.password)

      // if(this.adduserform.password!="111111"){
      //   ddform.append('password',this.adduserform.password)

      // }

      addform.append('email',this.adduserform.email)
      addform.append('tel',this.adduserform.tel)
      addform.append('wechat',this.adduserform.wechat)
      addform.append('is_superuser',this.adduserform.is_superuser)
      addform.append('is_active',this.adduserform.is_active)
      addform.append('is_staff',this.adduserform.is_staff)
      addform.append('first_name',this.adduserform.first_name)
      addform.append('last_name',this.adduserform.last_name)
      addform.append('person_type',this.adduserform.person_type)
      addform.append('avatar',this.adduserform.avatar?this.adduserform.avatar:"")

      request({
        url:"/users/users/",
        method:"post",
        headers:{"Content-Type":"multipart/form-data"},
        data:addform
      }).then(res=>{
        // 请求成功后的逻辑处理
        this.$message({
          message: '恭喜你，新增成功',
          type: 'success'
        });
        // 关闭模态框
        // this.addUserFormVisible = false;
        // 重新加载表格数据
        this.fetchUserData();
      }).catch(error=>{
        // 请求失败的逻辑处理
        console.log(error);
        this.$message({
          message: '新增失败',
          type: 'warning'
        });
        // 关闭模态框
        // this.addUserFormVisible = false;
      }).finally(()=>{
        // 关闭模态框
        this.addUserFormVisible = false;
      })
    },
    //编辑用户信息
    editUserInfo:function(){
      // 发起请求：新增用户-如果不涉及图片
      // request({url:"/users/users/",method:"post",data:this.adduserform}).then(res=>{
      //   // 请求成功后的逻辑处理
      // })
      // 发起请求：新增用户-涉及到文件上传（二进制流）
      /*
        FormData:用键值对模拟表单控件，用form表单控件中的name以及value值组成一个querystring
        作用：一般用来异步上传二进制文件
      */
      var editform = new FormData()
      editform.append('username',this.edituserform.username)
      editform.append('password',this.edituserform.password)

      // if(this.edituserform.password!="111111"){
      //   ddform.append('password',this.edituserform.password)

      // }

      editform.append('email',this.edituserform.email)
      editform.append('tel',this.edituserform.tel)
      editform.append('wechat',this.edituserform.wechat)
      editform.append('is_superuser',this.edituserform.is_superuser)
      editform.append('is_active',this.edituserform.is_active)
      editform.append('is_staff',this.edituserform.is_staff)
      editform.append('tel',this.edituserform.tel)
      editform.append('first_name',this.edituserform.first_name)
      editform.append('last_name',this.edituserform.last_name)
      editform.append('person_type',this.edituserform.person_type)
      editform.append('avatar',this.adduserform.avatar?this.adduserform.avatar:"")
      console.log(this.edituserform.id,"hhhhhhhhhhhhhhhhhhhhhhhh")

      request({
        url:"users/users/" + this.edituserform.id,
        method:"patch",
        headers:{"Content-Type":"multipart/form-data"},
        data:editform
      }).then(res=>{
        // 请求成功后的逻辑处理
        this.$message({
          message: '恭喜你，更改成功',
          type: 'success'
        });
        // 关闭模态框
        // this.editUserFormVisible = false;
        // 重新加载表格数据
        this.fetchUserData();
      }).catch(error=>{
        // 请求失败的逻辑处理
        console.log(error);
        this.$message({
          message: '更改失败',
          type: 'warning'
        });
        // 关闭模态框
        // this.editUserFormVisible = false;
      }).finally(()=>{
        // 关闭模态框
        this.editUserFormVisible = false;
      })
    },


    // 文件状态改变时的钩子，添加文件、上传成功和上传失败时都会被调用
    handlefileChange(file) {
      console.log(file)
      this.adduserform.avatar = file.raw
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    // 头像合法性校验
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!');
      }
      return isJPG && isLt2M;
    },
    // 每页显示的条目发生变化
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      this.params.page_size = val;
    },
    // 页码发生变化
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.params.page = val;
    },
    // 获取全部用户数据
    fetchUserData: function () {
      request({
        url: "/users/users/",
        method: "get",
        params: this.params,
      }).then((res) => {
        // 请求成功的处理
        console.log(res, "fetchUserData....");
        this.tableData = res.data.results;
        this.total_number = res.data.count;
      });
    },
    // 所需要的所有的方法定义在此处
    handleEdit(index, row) {
      // console.log(index);
      // console.log(row.id);
      // console.log("???");
      // 打开模态框
      this.editUserFormVisible = true;
      this.edituserform = row;
      // boolean类型的数据处理
      if(row.is_active){
        this.edituserform.is_active = "1"
      }else{
        this.edituserform.is_active = "0"
      }
      // if(row.is_superuser){
      //   this.edituserform.is_superuser = "1"
      // }else{
      //   this.edituserform.is_superuser = "0"
      // }
      this.edituserform.password = 111111;//默认后台未返回加密的字符串，给定默认值进行展示
      this.imageUrl = row.avatar;
      this.edituserform.id = row.id;
    },
    // 删除用户信息
    handleDelete(userid) {
      console.log(userid);
      this.$confirm("此操作将永久删除该用户, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          // 调用删除用户的接口将用户进行删除
          request({ url: "users/users/" + userid, method: "delete" }).then(
            (res) => {
              // 请求成功后的处理
              this.fetchUserData();
              this.$message({
                type: "success",
                message: "删除成功!",
              });
            }
          );
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
  },
};
</script>

<style>
/* scoped说明当前的样式修饰只针对当前组件有效 */
.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>

