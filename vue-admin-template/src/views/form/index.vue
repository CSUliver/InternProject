<template>
  <div class="app-container">
    //
    <div id='search' style='magin-buttom:15px'>
      {{searchtime}}
      <el-date-picker
        v-model="searchtime"
        type="datetimerange"
        :picker-options="pickerOptions"
        range-separator="至"
        start-placeholder="开始日期"
        end-placeholder="结束日期"
        align="right"
      >
      </el-date-picker>
    </div>
    <echartsline :linedata="tlinedata"></echartsline>
    <echartsline :linedata="slinedata"></echartsline>
    <echartsline></echartsline>
  </div>
</template>

<script>
import echartsline from "../../components/EchartsComponents/EchartsLine.vue";
import request from "../../utils/request.js";
export default {
  //应用组件
  components: {
    echartsline,
  },
  data() {
    return {
      tlinedata: {
        title: "温度折线图",
        legend: "温度",
        xdata: [],
        ydata: [],
        type: "line",
        color: "#ffb6b9",
      },
      slinedata: {
        title: "湿度折线图",
        legend: "湿度",
        xdata: [],
        ydata: [],
        type: "line",
        color: "#bbded6",
      },
      params:{},
      pickerOptions: {
          shortcuts: [{
            text: '最近一周',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
              picker.$emit('pick', [start, end]);
            }
          }, {
            text: '最近三个月',
            onClick(picker) {
              const end = new Date();
              const start = new Date();
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
              picker.$emit('pick', [start, end]);
            }
          }]
        },
        //js的newdata方法,默认值最近三天
        searchtime:['2021-08-11 00:00:00','2021-08-14 00:00:00']
    };
  },
  created() {
    this.fetchTempData();
  },
  //监听器
  watch:{
    searchtime:{
      handler:function(){
        this.fetchTempData();
      },
      deep:true
    }
  },
  methods: {
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
    fetchTempData() {
      this.tlinedata.xdata = [];
      this.tlinedata.ydata = [];
      request({
        url: "/devices/Air/",
        method: "get",
        params: {"start_time":this.formatDateTime(this.searchtime[0]),"end_time":this.formatDateTime(this.searchtime[1])},
      })
        .then((res) => {
          // console.log(res,"niub")
          res.data.results.forEach((item) => {
            this.tlinedata.xdata.push(item.addtime);
            this.tlinedata.ydata.push(item.Out_pressure);
          });
          console.log(this.tlinedata.xdata)
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.line {
  text-align: center;
}
</style>
