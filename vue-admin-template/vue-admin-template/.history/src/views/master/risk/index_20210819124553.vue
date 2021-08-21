<template>
  <div id="body">
    <!-- 页面左侧，为机场航班信息 -->
    <div id="left" style="width: 1000px; height: 600px; margin-top:10px">
      <!-- 1.搜索栏 -->
      <div id="search">
        {{params}}     
      <el-select
        v-model="params.infect_level"
        clearable
        placeholder="请选择感染风险等级">
        <el-option label="低风险" value="1"></el-option>
        <el-option label="中风险" value="2"></el-option>
        <el-option label="高风险" value="3"></el-option>
      </el-select>
        <el-date-picker
          v-model="params.start_time"
          type="datetimerange"
          :picker-options="pickerOptions"
          range-separator="至"
          start-placeholder="开始时间"
          end-placeholder="结束时间"
          align="right"
        >
        </el-date-picker>
      </div>

      <!-- 2.数据展示表格 -->
      <div id="datatable">
        <el-table border :data="tableData" style="width: 100%; margin-top: 15px"
        >
        <el-table-column label="风险事件id" width="100">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.id }}</span>
            </template>
          </el-table-column>
          <el-table-column label="感染风险等级" width="100">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.infect_level }}</span>
            </template>
          </el-table-column>
          <el-table-column label="发布时间">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.time }}</span>
            </template>
          </el-table-column>       
          <el-table-column label="监测点编号">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.monitor_id }}</span>
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
    this.fetchRiskData();
  },
  // 侦听器-监听器，用来动态刷新界面
  watch: {
    params: {
      handler: function (newparams, oldparams) {
        //时刻监听params数据的变化，一旦发生变化自动调用该方法
        console.log(newparams, oldparams,"changed");
        // 重新加载数据
        this.fetchRiskData();
      },
      deep: true, // 深度监听（对象或数据）
    },
  },
  methods: {
    // 获取风险信息
    fetchRiskData: function () {
      request({
        url: "/alarm​/riskdata​/",
        method: "get",
        params: this.params,
      }).then((res) => {
        // 请求成功的处理
        console.log(res, "fetchRiskData....");
        this.tableData = res.data.results;
        console.log(res.data.results, "res.data.results....");
        this.total_number = res.data.count;
        console.log(res.data.count, "res.data.count....");
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

