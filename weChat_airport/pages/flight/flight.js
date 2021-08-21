// pages/flight/flight.js
const _jwt = wx.getStorageSync('jwt_token')
const jwt = JSON.parse(_jwt)
var detail = 1
Page({

  /**
   * 页面的初始数据
   */
  data: {
    tableData: null,
    searchBeginValue:"",
    searchEndValue:""
  },
// 获取用户查询数据
  onBegin(e) {
    this.setData({
      searchBeginValue: e.detail,
    });
  },
  onEnd(e) {
    this.setData({
      searchEndValue: e.detail,
    });
  },

  onSearch:function(){
    let mid = this.search("departure",this.data.searchBeginValue,detail)
    if(mid.length == 0){
      wx.showToast({
        title: '无匹配航班',
        icon: 'fail',
        duration: 5000,
      })
    }
    else{
      let end = this.search("destination",this.data.searchEndValue,mid)
      if(end.length == 0){
        wx.showToast({
          title: '无匹配航班',
          icon: 'fail',
          duration: 5000,
        }) 
      }
      else{
        this.setData({
          tableData:end
        })
      }
    }
  },

  search :function(name,target,alllist){
    // console.log("subsearch0",name)
    // console.log("subsearch1",target)
    // console.log("subsearch2",alllist)
    let temp = []
    // 用户没有输入 全部显示
    if(target == ""){
      for (let i in alllist){
        temp.push(alllist[i])
      }
      return temp
    }
    for (let i in alllist){
      // console.log("subsearch3",alllist[i][departure])
      // console.log("subsearch4",alllist[i].departure)
      // console.log("subsearch5",alllist[i][name])
      if(alllist[i][name].indexOf(target)>=0){
        temp.push(alllist[i])
      }
    }
    return temp
  },

  //获取航班信息
  getFlight :function(){
    var that = this
    wx.request({
      url: "http://47.98.214.197:8000/flight/flightlist/",
      method: 'GET',
      header: {
        "Authorization" : "jwt " + jwt
      },
      dataType: "json",
      data: {		//向服务器发送的信息
        Token: jwt,
      },
      success: res => {
        console.log("success",res)
        const flight = res.data['results']
        // console.log("list",flight)
        detail = flight.map(item => {
        return {
          ...item
        }
      })
      // console.log("00",detail)
      // for(let i in detail){
      //   console.log("hhhh",detail[i])
      // }
      that.setData({
        tableData: detail,
      })
     
      }
    })
  },

  // 切换疫情界面
  infect: function () {
    console.log("go!")
    wx.navigateTo({
      url: '../infect/infect'
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.getFlight()
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

  }
})