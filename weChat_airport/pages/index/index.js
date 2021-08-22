// index.js
// 获取应用实例
const app = getApp()
var util = require ( '../../utils/util.js' );
let userid = 0;
let userstatus = ""

Page({
  data: {
    motto: '机场人员辅助系统',
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo'),
    canIUseGetUserProfile: false,
    canIUseOpenData: wx.canIUse('open-data.type.userAvatarUrl') && wx.canIUse('open-data.type.userNickName'), // 如需尝试获取用户信息可改为false
    show: false,
    columns: ['旅客人员', '机组人员', '机场工作人员'],
    columnstwo:['passenger','flight','airport'],
    uservalue:"",
    uservaluetwo:"",
    username:"passenger1",
    password:"admin123",
    userGet:{},
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
      uservalue:this.data.columns[index],
      uservaluetwo:this.data.columnstwo[index],
     });
     console.log(this.data.uservaluetwo)
  },
  onCancel(){
    this.setData({ show: false });
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
  // 切换注册界面
  register: function () {
    console.log("go!")
    wx.navigateTo({
      url: '../register/register'
    })
  },

  //用户登录，检查用户名与密码
  checkUser: function(e){		
    //与服务器进行交互
    wx.request({
      url: 'http://47.98.214.197:8000/login/',	//获取服务器地址
      header:{
        "content-type": "application/x-www-form-urlencoded"		//使用POST方法要带上这个header
      },
      method: "POST",
      data: {		//向服务器发送的信息
        username: this.data.username,
        password: this.data.password
      },
      success: res => {
        console.log("success1",res)
        if (res.statusCode == 200) {
          // console.log("success login",res)
          const _token = JSON.stringify(res.data.token)
          wx.setStorageSync('jwt_token', _token)
          const _jwt = wx.getStorageSync('jwt_token')
          const jwt = JSON.parse(_jwt)
          // console.log("jwt",jwt)
          wx.request({
            url: "http://47.98.214.197:8000/users/getinfo/",
            method: 'GET',
            header: {
              "Authorization" : "jwt " + jwt
            },
            dataType: "json",
            data: {		//向服务器发送的信息
              Token: jwt,
            },
            success: res => {
              console.log("success2",res)
              this.setData({
                userGet: res.data.results[0]	//服务器返回的结果
              })
              // 路由跳转
              if(this.data.userGet.person_type == this.data.uservaluetwo){
                userid = this.data.userGet.id
                userstatus = this.data.uservaluetwo
                let lasttime = this.data.userGet.last_login
                console.log("lasttime:",lasttime)
                if(lasttime==null){
                  wx.navigateTo({
                    url: '../login/login' + '?id=' + userid + '&status=' + userstatus
                })
                }
                else {
                  let formattime = lasttime.split("T")[0]
                  let nowtime = util.formatDate(new Date());
                  console.log("userid:", userid, "lasttime:", formattime, "nowtime:", nowtime)
                  if (formattime >= nowtime) {
                    console.log("go user!!")
                    console.log("state",this.data.uservaluetwo)
                    console.log('state2',userstatus)
                    navigateTo(userstatus)
                    // wx.navigateTo({
                    //   url: '../login/login' + '?id=' + userid + '&status=' + userstatus
                    // })
                  } else {
                    console.log("go login!!")
                    wx.navigateTo({
                      url: '../login/login' + '?id=' + userid + '&status=' + userstatus
                    })
                  }
                }
              }
              else{
                wx.showToast({
                  title: '身份不符',
                  icon: 'fail',
                  duration: 5000,
                })
              }
            }
          })
        }
        if (res.statusCode == 400) {
          wx.showToast({
            title: '用户名密码不匹',
            icon: 'fail',
            duration: 5000,
          })
        }
        
        // console.log("hhhh",this.data.result)
      }
    })
    
  },
  // 事件处理函数
  bindViewTap() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },
  onLoad() {
    if (wx.getUserProfile) {
      this.setData({
        canIUseGetUserProfile: true
      })
    }
    // let backtime = util.formatBackTime(new Date())
    // console.log("backtime",backtime)
  },
  getUserProfile(e) {
    // 推荐使用wx.getUserProfile获取用户信息，开发者每次通过该接口获取用户个人信息均需用户确认，开发者妥善保管用户快速填写的头像昵称，避免重复弹窗
    wx.getUserProfile({
      desc: '展示用户信息', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
      success: (res) => {
        console.log("getuserprofile",res)
        this.setData({
          userInfo: res.userInfo,
          hasUserInfo: true
        })
      }
    })
  },
  getUserInfo(e) {
    // 不推荐使用getUserInfo获取用户信息，预计自2021年4月13日起，getUserInfo将不再弹出弹窗，并直接返回匿名的用户个人信息
    console.log(e)
    this.setData({
      userInfo: e.detail.userInfo,
      hasUserInfo: true
    })
  },
})
function navigateTo(suburl) {
  console.log("suburl",suburl)
  let urlto = '../' + suburl +'/' + suburl
  console.log("url",urlto)
  wx.navigateTo({
      url: urlto + '?id=' + userid + '&status=' + userstatus
  })
}
