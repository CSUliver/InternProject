<template>
  <div id="body">
    <!-- 页面左侧，为机场航班信息 -->
    <div id="left" style="width: 1000px; height: 600px; margin-top:10px">
      <!-- 1.搜索栏 -->
      <div id="search">
        {{params}}
        <el-input
          style="margin-left: 10px; width: 300px; margin-right: 10px"
          placeholder="请输入关键字"
          v-model="params.search"
          clearable
        >
        </el-input>
        <el-date-picker
          v-model="params.searchtime"
          type="datetimerange"
          :picker-options="pickerOptions"
          range-separator="至"
          start-placeholder="起飞时间"
          end-placeholder="落地时间"
          align="right"
        >
        </el-date-picker>
      </div>

      <!-- 2.数据展示表格 -->
      <div id="datatable">
        <el-table
          border
          :data="tableData"
          style="width: 100%; margin-top: 15px"
        >
          <el-table-column label="编号" width="100">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.time }}</span>
            </template>
          </el-table-column>
          <el-table-column label="航空公司">
            <template slot-scope="scope">
                <span style="margin-left: 10px">{{ scope.row.person_type }}</span>
            </template>
          </el-table-column>
          <el-table-column label="始发地">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.person_id }}</span>
            </template>
          </el-table-column>
          <el-table-column label="目的地">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.person_name }}</span>
            </template>
          </el-table-column>
          <el-table-column label="起飞时间">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.person_temperature }}</span>
            </template>
          </el-table-column>
          <el-table-column label="落地时间">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.person_infect }}</span>
            </template>
          </el-table-column>
          <el-table-column label="落地时间">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.monitor_id }}</span>
            </template>
          </el-table-column>
          <el-table-column label="落地时间">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.staff_id }}</span>
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
    </div>

    
  </div>
</template>


<script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<script>
import { Form } from 'element-ui';
import request from "../../../utils/request.js";
export default {
  data() {
    return {
      pickerOptions: {
        shortcuts: [
          {
            text: "最近一周",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit("pick", [start, end]);
            },
          },
          {
            text: "最近一个月",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit("pick", [start, end]);
            },
          },
          {
            text: "最近三个月",
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit("pick", [start, end]);
            },
          },
        ],
      },
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
    };
  },
  // 初始化完成:data中的数据以及methods中的方法均可使用
  created() {
    this.fetchMonitorData();
  },
  // 侦听器-监听器，用来动态刷新界面
  watch: {
    params: {
      handler: function (newparams, oldparams) {
        //时刻监听params数据的变化，一旦发生变化自动调用该方法
        console.log(newparams, oldparams,"changed");
        // 重新加载数据
        this.fetchMonitorData();
      },
      deep: true, // 深度监听（对象或数据）
    },
  },
  methods: {
    // 获取航班信息
    fetchMonitorData: function () {
      request({
        url: "/monitor/monitordata/",
        method: "get",
        params: this.params,
      }).then((res) => {
        // 请求成功的处理
        console.log(res, "fetchMonitorData....");
        this.tableData = res.data.results;
        this.total_number = res.data.count;
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

