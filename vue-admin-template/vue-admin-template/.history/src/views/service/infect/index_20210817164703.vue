<template>
  <div class="hello">
    <!-- 2.数据展示表格 -->
      <div id="datatable">
        <el-table
          border
          :data="tableData"
          style="width: 100%; margin-top: 15px"
        >
          <el-table-column label="感染警示等级" width="200">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.alarm_level }}</span>
            </template>
          </el-table-column>
          <el-table-column label="警示时间">
            <template slot-scope="scope">
                <span style="margin-left: 10px">{{ scope.row.time }}</span>
            </template>
          </el-table-column>
          <el-table-column label="感染风险预警编号">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.risk_id }}</span>
            </template>
          </el-table-column>
          <el-table-column label="机场管理人员编号">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.staff_id }}</span>
            </template>
          </el-table-column>
        </el-table>
      </div>
    <!-- 疫情地图 -->
    <div ref="mapbox" style="height: 760px; width: 920px"></div>
  </div>
</template>

<script>
import china from "../../../components/EchartsComponents/china.json";
import jsonp from "jsonp";

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
  
  mounted() {
    //使用地图 需要先注册地图
    echarts.registerMap("china", china);
    this.getData();
    //创建mychart实例
    this.mychart = echarts.init(this.$refs.mapbox);
    this.mychart.setOption(option); //加载option
  },

  methods: {
    // 获取航班信息
    fetchInfectData: function () {
      request({
        url: "/alarm/riskdata/",
        method: "get",
        params: this.params,
      }).then((res) => {
        // 请求成功的处理
        console.log(res, "fetchInfectData....");
        this.tableData = res.data.results;
        this.total_number = res.data.count;
      });
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
