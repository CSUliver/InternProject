<template>
  <div id="body">
    <!-- 页面左侧，为机场航班信息 -->
    <div id="left" style="width: 1000px; height: 600px; margin-top:10px">
      <!-- 1.搜索栏 -->
      <div id="search">
        <!-- {{params}} -->
        <el-input
          style="margin-left: 10px; width: 500px; margin-right: 10px"
          placeholder="请输入受监测人员姓名"
          v-model="params.search"
          clearable
        >
        </el-input>
        <el-select
        v-model="params.person_type"
        clearable
        placeholder="请选择受监测人员类型">
        <el-option label="旅客" value="passenger"></el-option>
        <el-option label="机组人员" value="flight"></el-option>
        <!-- <el-option label="机场管理员" value="admin"></el-option> -->
        <el-option label="机场工作人员" value="airport"></el-option>
      </el-select>
      <el-select
        v-model="params.person_infect"
        clearable
        placeholder="请选择受监测人员状态">
        <el-option label="未感染" value="未感染"></el-option>
        <el-option label="无症状感染" value="无症状感染"></el-option>
        <el-option label="感染" value="感染"></el-option>
      </el-select>
        <el-date-picker
          v-model="searchtime"
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
        <el-table
          border
          :data="tableData"
          style="width: 100%; margin-top: 15px"
        >
        <el-table-column label="监测事件id" width="100">
            <template slot-scope="scope">
              <!-- <span style="margin-left: 10px">{{ scope.row.id }}</span> -->
              <el-tag v-if="scope.row.person_infect==='感染'" type="danger" effect="light">{{ scope.row.id }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='无症状感染'" type="warning" effect="light">{{ scope.row.id }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='未感染'" type="success" effect="light">{{ scope.row.id }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="监测时间" width="170">
            <template slot-scope="scope">
              <!-- <span style="margin-left: 10px">{{ scope.row.time }}</span> -->
              <el-tag v-if="scope.row.person_infect==='感染'" type="danger" effect="light">{{ scope.row.time }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='无症状感染'" type="warning" effect="light">{{ scope.row.time }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='未感染'" type="success" effect="light">{{ scope.row.time }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="受监测人员类型" width="130">
          <template slot-scope="scope">
            <el-tag v-if="scope.row.person_type==='admin'" type="success">机场管理员</el-tag>
            <el-tag v-else-if="scope.row.person_type==='passenger'">旅客</el-tag>
            <el-tag v-else-if="scope.row.person_type==='flight'" type="info">机组人员</el-tag>
            <el-tag v-else-if="scope.row.person_type==='airport'" type="warning">机场工作人员</el-tag>
            <span v-else>{{ scope.row.person_type }}</span>
          </template>
        </el-table-column>
          <el-table-column label="受监测人员id">
            <template slot-scope="scope">
              <!-- <span style="margin-left: 10px">{{ scope.row.person_id }}</span> -->
              <el-tag v-if="scope.row.person_infect==='感染'" type="danger" effect="light">{{ scope.row.person_id }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='无症状感染'" type="warning" effect="light">{{ scope.row.person_id }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='未感染'" type="success" effect="light">{{ scope.row.person_id }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="受监测人员姓名">
            <template slot-scope="scope">
              <!-- <span style="margin-left: 10px">{{ scope.row.person_name }}</span> -->
              <el-tag v-if="scope.row.person_infect==='感染'" type="danger" effect="light">{{ scope.row.person_name }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='无症状感染'" type="warning" effect="light">{{ scope.row.person_name }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='未感染'" type="success" effect="light">{{ scope.row.person_name }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="受检测人员体温">
            <template slot-scope="scope">
              <!-- <span style="margin-left: 10px">{{ scope.row.person_temperature }}</span> -->
              <el-tag v-if="scope.row.person_infect==='感染'" type="danger" effect="light">{{ scope.row.person_temperature }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='无症状感染'" type="warning" effect="light">{{ scope.row.person_temperature }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='未感染'" type="success" effect="light">{{ scope.row.person_temperature }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="感染状态">
            <template slot-scope="scope">
              <!-- <span v-if ="scope.row.person_infect==='感染'" style="margin-left: 10px">感染</span>
              <span v-else-if="scope.row.person_infect==='无症状感染'" style="margin-left: 10px">无症状感染</span>
              <span v-else-if="scope.row.person_infect==='未感染'" style="margin-left: 10px">未感染</span>
              <span v-else style="margin-left: 10px">{{ scope.row.person_infect }}</span> -->
              <el-tag v-if="scope.row.person_infect==='感染'" type="danger" effect="light">感染</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='无症状感染'" type="warning" effect="light">无症状感染</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='未感染'" type="success" effect="light">未感染</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="监测点编号">
            <template slot-scope="scope">
              <!-- <span style="margin-left: 10px">{{ scope.row.monitor_id }}</span> -->
              <el-tag v-if="scope.row.person_infect==='感染'" type="danger" effect="light">{{ scope.row.monitor_id }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='无症状感染'" type="warning" effect="light">{{ scope.row.monitor_id }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='未感染'" type="success" effect="light">{{ scope.row.monitor_id }}</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="执勤人员编号">
            <template slot-scope="scope">
              <!-- <span style="margin-left: 10px">{{ scope.row.staff_id }}</span> -->
              <el-tag v-if="scope.row.person_infect==='感染'" type="danger" effect="light">{{ scope.row.staff_id }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='无症状感染'" type="warning" effect="light">{{ scope.row.staff_id }}</el-tag>
              <el-tag v-else-if="scope.row.person_infect==='未感染'" type="success" effect="light">{{ scope.row.staff_id }}</el-tag>
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
      //js的newdata方法,默认值最近三天
      searchtime:['2021-08-14T16:00:00.000Z','2021-08-30T16:00:00.000Z'],
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
    searchtime:{
      handler:function(){
      this.fetchMonitorData();
      },
      deep:true
    }
  },
  methods: {
    // 获取航班信息
    fetchMonitorData: function () {
      request({
        url: "/monitor/monitordata/",
        method: "get",
        // params: this.params,
        params: {"page":this.params.page,"page_size":this.params.page_size,
                "start_time":this.formatDateTime(this.searchtime[0]),
                "search":this.params.search,
                "person_infect":this.params.person_infect,
                "end_time": this.formatDateTime(this.searchtime[1])},
      }).then((res) => {
        // 请求成功的处理
        console.log(res, "fetchMonitorData....");
        this.tableData = res.data.results;
        this.total_number = res.data.count;
      });
    },
        //时间格式转化函数
    formatDateTime(date) {
        const time = new Date(Date.parse(date));
        console.log('time',time)
        time.setTime(time.setHours(time.getHours() + 8));
        const Y = time.getFullYear() + '-';//2021.
        //x<10?y:z
        const M = (time.getMonth() + 1) < 10 ? '0' + (time.getMonth() + 1) + '-' : (time.getMonth() + 1) + '-';//05.   10.
        const D = (time.getDate()) < 10 ? '0' + (time.getDate()) + ' ' : (time.getDate()) + ' ';
        const h = (time.getHours()) < 10 ? '0' + (time.getHours()) + ':' : (time.getHours()) + ':';
        const m = (time.getMinutes()) <10 ? '0' + (time.getMinutes()) + ':' : (time.getMinutes()) + ':';
        const s = (time.getSeconds()) < 10 ? '0' + (time.getSeconds()) : (time.getSeconds());
        return Y + M + D + h + m + s;//2021-12-12 12:12:12
    },
        // 所需要的所有的方法定义在此处
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
