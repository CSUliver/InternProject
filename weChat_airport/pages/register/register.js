// pages/register/register.js
const app = getApp()
var util = require ( '../../utils/util.js' );
const _jwt = wx.getStorageSync('jwt_token')
const jwt = JSON.parse(_jwt)
let WXMap = require("../../libs/qqmap-wx-jssdk.min")
let mapApi
Page({

  /**
   * 页面的初始数据
   */
  data: {
    username:"",
    password:"",
    tel:"",
    usercolumns: ['旅客人员', '机组人员', '机场工作人员'],
    usercolumnstwo:['passenger','flight','airport'],
    uservalue:"",
    uservaluetwo:"",
    codecolumns: ['绿色', '黄色', '红色'],
    codecolumnstwo:["1","2","3"],
    codevalue:"",
    codevaluetwo:"",
  },
  // 健康码弹出层函数
  showCodePopup() {
    this.setData({ Codeshow: true });
  },
  onCodeClose() {
    this.setData({ Codeshow: false });
  },
  //健康码选择器函数
  onCodeConfirm(res) {
    //切换健康码类别
    let index = res.detail.index
    this.setData({ 
      Codeshow: false,
      codevalue:this.data.codecolumns[index],
      codevaluetwo:this.data.codecolumnstwo[index],
     });
     console.log(this.data.codevalue)
  },
  onCodeCancel(){
    this.setData({ Codeshow: false });
  },

  // 用户类别弹出层函数
  showUserPopup() {
    this.setData({ Usershow: true });
  },
  onUserClose() {
    this.setData({ Usershow: false });
  },
  //用户类别选择器函数
  onUserConfirm(res) {
    //切换用户类别
    let index = res.detail.index
    this.setData({ 
      Usershow: false,
      uservalue:this.data.usercolumns[index],
      uservaluetwo:this.data.usercolumnstwo[index],
     });
     console.log(this.data.uservalue)
  },
  onUserCancel(){
    this.setData({ Usershow: false });
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
  //用户信息上传
  updateUser(){
    var that = this
    let backtime = util.formatBackTime(new Date())
    wx.request({
      url: "http://47.98.214.197:8000/users/app/",
      method: 'POST',
      data: {		//向服务器发送的信息
        username:that.data.username,
        password:that.data.password,
        tel:that.data.tel,
        person_type:that.data.uservaluetwo,
        is_active:1,
        infect_level:that.data.codevaluetwo,
        last_login:backtime
        // id:that.data.id,
      },
      success: res => {
        console.log("success",res)
        wx.showModal({
          title: '提示',
          content: '用户创建成功，是否跳转',
          success: function (res) {
            if (res.confirm) {
             console.log('用户点击确定')
             wx.navigateTo({
              url: '../index/index'
          })
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