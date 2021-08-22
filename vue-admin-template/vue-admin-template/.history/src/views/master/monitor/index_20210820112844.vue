<template>
  <div id="body">
    <!-- 页面左侧，为机场航班信息 -->
    <div id="new" style="width: 100px; height: 600px; margin-top:10px">
      <el-button
        type="primary"
        plain
        style="float: right"
        @click="addFormVisible = true;addform={}"
        >新增监测点</el-button
      >
      </div>
      <!-- 2.数据展示表格 -->
      <div id="datatable">
        <el-table
          border
          :data="tableData"
          style="width: 100%; margin-top: 100px"
        >
        <el-table-column label="监测点编号" >
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.id }}</span>
            </template>
          </el-table-column>
          <el-table-column label="监测点位置" >
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.position }}</span>
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
    <el-dialog title="新增监测点" :visible.sync="addFormVisible">
      <!-- {{addform}}  -->
      <el-form :model="addform">
        <el-form-item label="监测点位置" :label-width="formLabelWidth">
          <el-input
            v-model="addform.position"
            autocomplete="off"
          ></el-input>
        </el-form-item>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="addFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="addInfo"
          >确 定</el-button
        >
      </div>
    </el-dialog>

    <!-- 编辑用户模态框 -->
    <el-dialog title="编辑用户" :visible.sync="editFormVisible">
      <!-- {{edituserform}}  -->
      <el-form :model="editform">
        <el-form-item label="监测点编号" :label-width="formLabelWidth">
          <el-input
            v-model="editform.id"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item label="监测点位置" :label-width="formLabelWidth">
          <el-input 
            v-model="editform.position"
            autocomplete="off"
          ></el-input>
        </el-form-item>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="editFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="editInfo"
          >确 定</el-button
        >
      </div>
    </el-dialog>
    
  </div>
</template>


<script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script>
import { Form } from 'element-ui';
import request from "../../../utils/request.js";
export default {
  data() {
    return {
      // 所有的数据变量定义在此处
      value: "",
      input: "",
      // 表格数据
      params: {
        page: 1, // 默认显示第一页
        page_size: 5, // 默认每页显示的条数
      },
      formLabelWidth: "120px",
      tableData: [],
      total_number: 0, // 数据总条数
      addFormVisible: false,
      editFormVisible: false,
      formLabelWidth: "120px",
      addform: {},
      // 编辑用户表单数据
      editform:{},
    };
  },
  // 初始化完成:data中的数据以及methods中的方法均可使用
  created() {
    this.fetchMonitorlistData();
  },
  // 侦听器-监听器，用来动态刷新界面
  watch: {
    params: {
      handler: function (newparams, oldparams) {
        //时刻监听params数据的变化，一旦发生变化自动调用该方法
        console.log(newparams, oldparams,"changed");
        // 重新加载数据
        this.fetchMonitorlistData();
      },
      deep: true, // 深度监听（对象或数据）
    },
  },
  methods: {
    // 获取航班信息
    fetchMonitorlistData: function () {

      request({
        url: "/monitor/monitorlist/",
        method: "get",
        params: this.params,
      }).then((res) => {
        // 请求成功的处理
        console.log(res, "fetchMonitorlistData....");
        this.tableData = res.data.results;
        this.total_number = res.data.count;
      });
    },
    addInfo:function(){
      var addform = new FormData()
      addform.append('position',this.addform.position)
      request({
        url:"/monitor/monitorlist/",
        method:"post",
        headers:{"Content-Type":"multipart/form-data"},
        data:addform
      }).then(res=>{
        this.$message({
          message: '恭喜你，新增成功',
          type: 'success'
        });
        this.fetchMonitorlistData();
      }).catch(error=>{
        console.log(error);
        this.$message({
          message: '新增失败',
          type: 'warning'
        });
      }).finally(()=>{
        this.addFormVisible = false;
      })
    },
    editInfo:function(){
      var editform = new FormData()
      editform.append('id',this.editform.id)
      editform.append('position',this.editform.position)
      console.log(this.editform.id,"hhhhhhhhhhhhhhhhhhhhhhhh")

      request({
        url:"/monitor/monitor/" + this.editform.id,
        method:"patch",
        headers:{"Content-Type":"multipart/form-data"},
        data:editform
      }).then(res=>{
        // 请求成功后的逻辑处理
        this.$message({
          message: '恭喜你，更改成功',
          type: 'success'
        });
        this.fetchMonitorlistData();
      }).catch(error=>{
        console.log(error);
        this.$message({
          message: '更改失败',
          type: 'warning'
        });
      }).finally(()=>{
        this.editFormVisible = false;
      })
    },
    // 所需要的所有的方法定义在此处
    handleEdit(index, row) {
      this.editFormVisible = true;
      this.editform = row;
      this.editform.id = row.id;
    },
    // 删除用户信息
    handleDelete(userid) {
      console.log(userid);
      this.$confirm("此操作将永久删除该监测点, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          // 调用删除用户的接口将用户进行删除
          request({ url: "/monitor/monitor/" + userid, method: "delete" }).then(
            (res) => {
              // 请求成功后的处理
              this.fetchMonitorlistData();
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
  },
};
</script>

<style>
#body {
  display: flex !important;
  position:absolute;
  display: flex;
  display: -webkit-flex;
  align-items:center;
  justify-content:center;
  flex: 1;
}
/* scoped说明当前的样式修饰只针对当前组件有效 */
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
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
