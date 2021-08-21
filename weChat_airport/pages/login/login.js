// pages/login/login.js
const app = getApp()
var util = require ( '../../utils/util.js' );
let WXMap = require("../../libs/qqmap-wx-jssdk.min")
let mapApi
const _jwt = wx.getStorageSync('jwt_token')
const jwt = JSON.parse(_jwt)
let userid = 0;
let userstatus = ""
Page({

  /**
   * 页面的初始数据
   */
  data: {
    username:"",
    password:"",
    tel:"",
    columns: ['绿色', '黄色', '红色'],
    columnstwo:["1","2","3"],
    colorlist:['#00ff00','#ffdb00','#ff0000'],
    color:"#000000",
    codevalue:"",
    codevaluetwo:"",
    imagepath:"",
    mapvalue:"",
  },
  // 弹出层函数
  showPopup() {
    this.setData({ show: true });
  },
  onClose() {
    this.setData({ show: false });
  },
  //选择器函数
  onConfirm(res) {
    //切换用户类别
    let index = res.detail.index
    this.setData({
      show: false,
      codevalue: this.data.columns[index],
      codevaluetwo: this.data.columnstwo[index],
      color:this.data.colorlist[index],
    });
    console.log("codevalue",this.data.codevaluetwo)
    // console.log(this.data.color)
  },
  onCancel() {
    this.setData({
      show: false
    });
  },
  // 获取用户名
  getUserName(event){
    this.setData({
      username:event.detail
    })
    console.log(this.data.username)
  },
  // 获取用户密码
  getUserPass(event){
    this.setData({
      password:event.detail
    })
    console.log(this.data.password)
  },
  // 获取用户电话
  getUserTele(event){
    this.setData({
      tel:event.detail
    })
    console.log(this.data.tel)
  },
  // 选择图片
  selectImg(){
    wx.chooseImage({
      success:(res)=>{
        console.log(res),
        this.setData({
          imagepath:res.tempFilePaths[0]//设置图片路径
        })
      },
    })
  },
  // 获取位置
  selectLocation(){
    let that = this
    wx.getLocation({
      type:"wgs84",
      success(res){
        console.log(res)
        mapApi.reverseGeocoder({
          location: {
          latitude: res.latitude,
          longitude: res.longitude
          },
          success: function (rres) {
          console.log(rres.result);
          that.setData({
            mapvalue:rres.result.ad_info.name
          })
          },
        })
      }
    })
  },

  //获取用户信息
  getUser :function(){
    var that = this
    wx.request({
      url: "http://47.98.214.197:8000/users/app/"+userid,
      method: 'GET',
      header: {
        "Authorization" : "jwt " + jwt
      },
      dataType: "json",
      data: {		//向服务器发送的信息
        Token: jwt,
      },
      success: res => {
        console.log("successget",res)
      that.setData({
        username: res.data.username,
        tel:res.data.tel,
      })
     
      }
    })
  },

  updateUser(){
    var that = this
    let backtime = util.formatBackTime(new Date())
    wx.request({
      url: "http://47.98.214.197:8000/users/app/"+userid,
      method: 'PUT',
      header: {
        "Authorization" : "jwt " + jwt,
      },
      data: {		//向服务器发送的信息
        Token: jwt,
        username:that.data.username,
        password:that.data.password,
        infect_level:that.data.codevaluetwo,
        tel:that.data.tel,
        person_type:userstatus,
        is_active:1,
        last_login:backtime
        // id:userid,
      },
      success: res => {
        console.log(res)
        wx.showModal({
          title: '提示',
          content: '信息提交成功，是否跳转',
          success: function (res) {
            if (res.confirm) {
             console.log('用户点击确定')
             navigateTo(userstatus)
           }
          }
        })

      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    mapApi = new WXMap({
      key:"RARBZ-QXM6S-BHZO2-6H5KD-5H3FH-T4BYK"
    })
    userid = options.id,
    userstatus = options.status,
    console.log("id:",userid,"status:",userstatus)
    this.getUser();
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
function navigateTo(suburl) {
  console.log("suburl",suburl)
  let urlto = '../' + suburl +'/' + suburl
  console.log("url",urlto)
  wx.navigateTo({
      url: urlto + '?id=' + userid + '&status=' + userstatus
  })
}