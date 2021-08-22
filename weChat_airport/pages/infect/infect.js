// pages/passenger/passenger.js
import * as echarts from '../../ec-canvas/echarts';
import china from './mapData';


Page({

  /**
   * 页面的初始数据
   */
  data: {
    data: null,
    ec: {},
    tableData: null,
    dataList: [],
  },

  //  页面相关事件处理函数--监听用户下拉动作
  onPullDownRefresh: function () {
    //调用刷新时将执行的方法
    this.getCountry();
    this.loadData();
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.oneComponent = this.selectComponent('#mychart-dom-area');
    this.getCountry();
    this.loadData();
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  },
  // 获取全国疫情数据
  getCountry: function () {
    var that = this
    wx.$api.getOnsInfo().then(res => {
      //停止下拉刷新
      wx.stopPullDownRefresh();
      const data = JSON.parse(res.data);
      console.log(data)
      const areaTree = data['areaTree']
      const china = areaTree[0]
      var list = [{
        name: "今日确诊",
        class: "todayConfirmed",
        data: china.today.confirm,
      },{
        name: "当前确诊",
        class: "nowConfirmed",
        data: china.total.nowConfirm,
      },{
        name: "累计确诊",
        class: "totalConfirmed",
        data: china.total.confirm,
      }, {
        name: "累计死亡",
        class: "totalDeath",
        data: china.total.dead,
      }]
      that.setData({
        dataList: list
      })
    })
  },
  // 加载全国疫情地图
  initChart: function () {
    this.oneComponent.init((canvas, width, height) => {
      const chart = echarts.init(canvas, null, {
        width: width,
        height: height
      });
      canvas.setChart(chart);
      echarts.registerMap('china', china);

      const option = {
        toolbox: {
          show: true,
          orient: "vertical",
          left: "right",
          top: "center",
          feature: {
            dataView: { readOnly: false },
            restore: {},
          },
        },
        tooltip: {
          trigger: "item", //设置鼠标滑过，提示多少人
          formatter: "{b}{c}",
        },

        visualMap: {
          show: true,
          type: "piecewise",
          left: 10,
          bottom: "0",
          align: "left",
          itemWidth: 10,
          itemHeight: 10,
          textStyle: {
            fontSize: 10
          },
          pieces: [{
              min: 1000,
              label: '1000人以上',
              color: '#ED514E'
            },
            {
              min: 100,
              max: 999,
              label: '100-999人',
              color: '#FF8F66'
            },
            {
              min: 10,
              max: 99,
              label: '10-99人',
              color: '#FFB769'
            },
            {
              min: 1,
              max: 9,
              label: '1-9人',
              color: '#FFE6BD'
            },
            {
              max: 1,
              label: '1人以下',
              color: '#FFF4E1'
            }
          ]
        },
        series: [{
          name: "确诊人数",
          type: 'map',
          mapType: 'china',
          label: {
            show: true,
            fontSize: 8
          },
          itemStyle: {
            normal: {
              borderColor: '#eaeaea',
              areaColor: '#fff',
            },
            emphasis: {
              areaColor: '#389BB7',
              borderWidth: 0
            }
          },
          animation: false,
          data: this.data.data
        }]
      };
      chart.setOption(option);

      return chart;
    });
  },
  //加载数据
  loadData: function () {
    var that = this
    wx.$api.getOnsInfo().then(res => {
      const data = JSON.parse(res.data);
      console.log(data)
      const areaTree = data['areaTree']
      const china = areaTree[0]
      const provinces = china['children']
      // console.log("list",provinces)
      const provincesData = provinces.map(item => {
        return {
          name: item.name,
          value: item.total.nowConfirm
        }
      })
      const detail = provinces.map(item => {
        return {
          area: item.name,
          ...item.total
        }
      })
      console.log("----", detail)
      that.setData({
        data: provincesData,
        tableData: detail,
      })
      that.initChart()
    })
  },
})