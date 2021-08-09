<template>
  <div class="app-container">
    <!-- 模板 -->
    <!-- 1.搜索栏 -->
    <div id="search">
      <el-input
        style="width: 300px; margin-right: 10px"
        placeholder="请输入关键字"
        v-model="input"
        clearable
      >
      </el-input>
      <el-select v-model="value" clearable placeholder="请选择">
        <el-option label="冻结" value="1"></el-option>
        <el-option label="活跃" value="0"></el-option>
      </el-select>
      <el-button type="primary" plain style="float: right">新增用户</el-button>
    </div>

    <!-- 2.数据展示表格 -->
    <div id="datatable">
      <el-table border :data="tableData" style="width: 100%; margin-top: 15px">
        <el-table-column label="编号" width="80">
          <template slot-scope="scope">
            <span style="margin-left: 10px">{{ scope.$index + 1 }}</span>
          </template>
        </el-table-column>
        <el-table-column label="邮箱" >
          <template slot-scope="scope">
            <i class="el-icon-time"></i>
            <span style="margin-left: 10px">{{ scope.row.email }}</span>
          </template>
        </el-table-column>
        <el-table-column label="用户账号" >
          <template slot-scope="scope">
            <el-popover trigger="hover" placement="top">
              <p>姓名: {{ scope.row.username }}</p>
              <p>编号: {{ scope.row.id }}</p>
              <div slot="reference" class="name-wrapper">
                <el-tag size="medium">{{ scope.row.username }}</el-tag>
              </div>
            </el-popover>
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
    <!-- <div id="pagenations">
      <el-pagination style="float:right;margin-top:15px;" background
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage4"
        :page-sizes="[100, 200, 300, 400]"
        :page-size="100"
        layout="total, sizes, prev, pager, next, jumper"
        :total="400"
      >
      </el-pagination>
    </div> -->
  </div>
</template>

<script>
import request from '../../utils/request.js'
export default {
  data() {
    return {
      // 所有的数据变量定义在此处
      value: "",
      input: "",
      // 表格数据
      tableData: [],
    };
  },
  // 初始化完成:data中的数据以及methods中的方法均可使用
  created(){

    this.fetchUserData();
  },
  methods: {
    // 获取前部用户数据
    fetchUserData:function(){
        request({
          url:"/users/users/",
          method:"get"
        }).then(res=>{
          // 请求成功的处理
          console.log(res,'fetchUserData....')
          this.tableData = res.data.results
        })
    },
    // 所需要的所有的方法定义在此处
    handleEdit(index, row) {
      console.log(index, row);
    },
    // 删除用户信息
    handleDelete(userid) {
      console.log(userid)
      this.$confirm('此操作将永久删除该用户, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          // 调用删除用户的接口将用户进行删除
          request({url:"users/users/"+userid,method:"delete"}).then(res=>{
            // 请求成功后的处理
            this.fetchUserData();
            this.$message({
              type: 'success',
              message: '删除成功!'
            });
          })
          
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });          
        });
    },
  },
};
</script>

<style scoped>
/* scoped说明当前的样式修饰只针对当前组件有效 */
</style>
