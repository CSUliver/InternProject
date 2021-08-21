<template>
  <div class="hello">
    <div id="search">
      <el-select
        v-model="params.alarm_level"
        clearable
        placeholder="请选择感染警示等级">
        <el-option label="中风险" value="2"></el-option>
        <el-option label="高风险" value="3"></el-option>
      </el-select>

        <el-date-picker
          v-model="searchtime"
          type="datetimerange"
          :picker-options="pickerOptions"
          range-separator="至"
          start-placeholder=""
          end-placeholder=""
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
          <el-table-column label="感染警示等级" width="200">
            <template slot-scope="scope">
              <!-- <span v-if="scope.row.alarm_level==='1'" style="margin-left: 10px">{{ "低风险" }}</span> -->
              <!-- <span v-if="scope.row.alarm_level==='2'" style="margin-left: 10px">{{ "中风险" }}</span>
              <span v-else-if="scope.row.alarm_level==='3'" style="margin-left: 10px">{{ "高风险" }}</span>  -->
            <el-tag v-if="scope.row.alarm_level==='2'" effect="light" type="warning">中风险</el-tag>
            <el-tag v-else-if="scope.row.alarm_level==='3'" effect="light" type="danger">高风险</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="警示时间">
            <template slot-scope="scope">
                <span style="margin-left: 10px">{{ scope.row.time }}</span>
            </template>
          </el-table-column>
          <el-table-column label="感染风险预警编号">
            <template slot-scope="scope">
              <el-tag type="success" effect="light">{{scope.row.risk_id}}</el-tag>
            
              <!-- <span style="margin-left: 10px">{{ scope.row.risk_id }}</span> -->
            </template>
          </el-table-column>
          <el-table-column label="机场管理人员编号">
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
    <!-- 疫情地图 -->
    <div ref="mapbox" style="height: 760px; width: 920px; margin-top: 150px"></div>
  </div>
</template>

<script>
import china from "../../../components/EchartsComponents/china.json";
import jsonp from "jsonp";
import { Form } from 'element-ui';
import request from "../../../utils/request.js";
const option = {
  title: {
    text: "最新疫情地图", //显示标题
  },
  series: [
    {
      name: "确诊人数", //鼠标移动提示文字 在显示人数上面
      type: "map", //告诉echarts 要去渲染地图
      mapType: "china", //告诉echart 要去渲染中国地图
      label: {
        //控制显示对于地区的汉字
        show: true,
        color: "gray", //控制地区名的字体颜色
        fontSize: 10,
      },
      itemStyle: {
        areaColor: "white", //设置地图背景色
        borderColor: "light gray", //设置地图边线颜色
      },
      roam: true, //支持滚轮放大缩小 以及拖拽
      zoom: 1.2, //控制地图的放大和缩小
      emphasis: {
        //控制鼠标滑过之后的背景色和字体颜色
        label: {
          color: "#fff",
          fontSize: 12,
        },
        itemStyle: {
          areaColor: "#83b5e7",
          borderColor: "black",
        },
      },
      data: [], //用来展示后台给的数据
    },
  ],
  visualMap: [
    {
      type: "piecewise",
      show: true,
      pieces: [
        //分段
        { min: 1000 },
        { min: 101, max: 1000 },
        { min: 11, max: 100 },
        { min: 6, max: 10 },
        { min: 1, max: 5 },
        { max:1 },
      ],
      // orient:'horizontal' //修改横向显示 默认垂直显示
      inRange: {
        symbol: "rect", //显示数据方块小图标形状
        color: ["#ffffff", "#9c0505"], // 显示颜色
      },
    },
  ],
  toolbox: {
    show: true,
    orient: "vertical",
    left: "right",
    top: "center",
    feature: {
      dataView: { readOnly: false },
      restore: {},
      saveAsImage: {},
    },
  },
  tooltip: {
    trigger: "item", //设置鼠标滑过，提示多少人
    formatter: "{b}<br/>{c}",
  },
};


export default {
  name: "HelloWorld",
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
          }],
      },
      //js的newdata方法,默认值最近三天
      searchtime:['2021-06-02T16:00:00.000Z','2021-08-20T16:00:00.000Z'],
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
    this.fetchInfectData();
  },
  // 侦听器-监听器，用来动态刷新界面
  mounted() {
    //使用地图 需要先注册地图
    echarts.registerMap("china", china);
    this.getData();
    //创建mychart实例
    this.mychart = echarts.init(this.$refs.mapbox);
    this.mychart.setOption(option); //加载option
  },
  watch: {
    params: {
      handler: function (newparams, oldparams) {
        //时刻监听params数据的变化，一旦发生变化自动调用该方法
        console.log(newparams, oldparams,"changed");
        // 重新加载数据
        this.fetchInfectData();
      },
      deep: true, // 深度监听（对象或数据）
    },
    searchtime:{
      handler:function(){
      this.fetchInfectData();
      },
      deep:true
    }
  },

  methods: {
    // 获取航班信息
    fetchInfectData: function () {
      request({
        url: "/alarm/alarmdata/",
        method: "get",
        // params: this.params,
        params: {"page":this.params.page,"page_size":this.params.page_size,
                "alarm_level":this.params.alarm_level,
                "start_time":this.formatDateTime(this.searchtime[0]),
                "end_time": this.formatDateTime(this.searchtime[1])},
      }).then((res) => {
        // 请求成功的处理
        console.log(res, "fetchInfectData....");
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

    getData() {
      jsonp(
        "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5",
        {},
        (err, data) => {
          if (!err) {
            // console.log("fetchInfectdata1", data);
            var res = data.data || "";
            res = JSON.parse(res);
            // console.log("fetchInfectdata2",res);
            // console.log("fetchInfectdata3", res.areaTree[0].children);
            //代表数据请求成功
            let list = res.areaTree[0].children.map((item) => ({
              name: item.name,
              value: item.total.nowConfirm,
            }));
            // console.log("fetchInfectdata4", list);
            option.series[0].data = list; //将数据赋给series里面的data然后进行渲染
            //能够执行的前提是DOM已经渲染完成，只有DOM渲染完成才能够执行echarts的初始化
            this.mychart.setOption(option);
          }
        }
      );
    },

  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
