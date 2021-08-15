<template>
  <div>
    <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
    <div>

    </div>
    <div ref="main" style="width: 600px; height: 400px"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      option: {
        title: {
          text: this.linedata.title
        },
        tooltip: {
          trigger: "axis",
        },
        legend: {
          data: this.linedata.legend,
        },
        xAxis: {
          data: this.linedata.xdata,
          type:"category",
          boundaryGap:false,
        },
        yAxis: {},
        series: [
          {
            name: this.linedata.legend,
            type: this.linedata.type,
            data: this.linedata.ydata,
            areaStyle:{},
            itemStyle:{
                color:this.linedata.color
            }
          },
        ],
      },
    };
  },
  //当前组件参数
  props:[
      'linedata'
  ],
  watch:{
    linedata:{
      handler:function(){
        //进行搜索时数据不统一，需要重新赋值
        // console.log(this.linedata.xdata,'yyy')
        // console.log(this.option.xAxis.xdata,'xxx')\
        this.option.xAxis.data = this.linedata.xdata;
        this.option.series[0].data = this.linedata.ydata;
        this.DrawLine()
      },
      deep:true //深度监听
    }
  },
  mounted() {
    this.DrawLine();
  },
  methods: {
    //绘制图表
    DrawLine: function () {
      // 基于准备好的dom，初始化echarts实例
      // var myChart = echarts.init(document.getElementById('main'));
      var myChart = echarts.init(this.$refs.main);
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(this.option);
    },
  },
};
</script>

<style>
</style>
