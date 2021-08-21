// pages/airport/airport.js
const _jwt = wx.getStorageSync('jwt_token')
const jwt = JSON.parse(_jwt)
var dateTimePicker = require('../../utils/dateTimePicker.js');
var detail = 1
Page({

  /**
   * 页面的初始数据
   */
  data: {
    tableData: null,
    searchBeginValue:"",
    searchEndValue:"",
    date: '2018-10-01',
    time: '12:00',
    dateTimeArray: null,
    Startvalue:"",
    Endvalue:"",
    startYear: 2000,
    endYear: 2050
  },
  // 时间格式切换函数
  Timeformat:function(origintime){
    // console.log(origintime)
    let temp1 = []
    let temp2 = []
    let num = (origintime.length)/2
    for (let i in origintime){
      if(i<=2){
        if(origintime[i]>=10){
          temp1.push(origintime[i])
        }
        else{
          temp1.push("0"+origintime[i])
        }
        
        // 需要加Number()str转int，要不然会字符拼接，我也不知道为什么
        let j = num + Number(i)
        if(origintime[j]<10){
          temp2.push("0"+origintime[j])
        }
        else{
          temp2.push(origintime[j])
        }
      }
    }
    console.log(temp1)
    let str1 = temp1.join("-")
    let str2 = temp2.join(":")
    let formattime = "20" + str1 + " " + str2
    return formattime
  },
  // 开始时间弹出层函数
  showStartPopup() {
    this.setData({ Startshow: true });
  },
  onStartClose() {
    this.setData({ Startshow: false });
    // console.log("startend",this.data.Startvalue)
    // let newtime = this.Timeformat(this.data.Startvalue)
    // console.log("startendend:",newtime)
  },
  // 结束时间弹出层函数
  showEndPopup() {
    this.setData({ Endshow: true });
  },
  onEndClose() {
    this.setData({ Endshow: false });
    // console.log("endend",this.data.Endvalue)
  },

  onSearch:function(){
    let begin = this.data.searchBeginValue;
    let end = this.data.searchEndValue;
    console.log("start:",begin,"end:",end)
    if(begin=="" || end ==""){
      wx.showToast({
        title: '起止时间需完整',
        icon: 'fail',
        duration: 5000,
      })
    }
    else{
      let temp = []
      for(let i in detail){
        if(detail[i].time>=begin && detail[i].time<=end){
          temp.push(detail[i])
        }
      }
      if(temp.length == 0){
        wx.showToast({
          title: '无匹配任务',
          icon: 'fail',
          duration: 5000,
        }) 
      }
      else{
        this.setData({
          tableData:temp
        })
      }
    }

  },

  //获取任务信息
  getTask :function(){
    var that = this
    wx.request({
      url: "http://47.98.214.197:8000/task/tasklist/",
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
        const task = res.data['results']
        console.log("list",task)
        detail = task.map(item => {
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
    this.getTask()
     // 获取完整的年月日 时分秒，以及默认显示的数组
     var obj = dateTimePicker.dateTimePicker(this.data.startYear, this.data.endYear);
     
     this.setData({
       Startvalue: obj.dateTime,
       Endvalue: obj.dateTime,
       dateTimeArray: obj.dateTimeArray,
     });
  },
  changeStartDateTime(e){
    console.log("changeStartDateTime")
    this.setData({ 
      Startshow: false
     });
  },
  changeStartDateTimeColumn(e){
    console.log("changeStartDateTimeColumn")
    var arr = this.data.Startvalue, dateArr = this.data.dateTimeArray;
    console.log(e)
    if(e.detail.column==1 || e.detail.column==2){
      arr[e.detail.column] = e.detail.value+2;
    }
    else{
      arr[e.detail.column] = e.detail.value;
    }
    dateArr[2] = dateTimePicker.getMonthDay(dateArr[0][arr[0]], dateArr[1][arr[1]]);
    let newtime = this.Timeformat(arr)
    this.setData({
      dateTimeArray: dateArr,
      Startvalue: arr,
      searchBeginValue:newtime
    });
  },
  changeEndDateTime(e){
    console.log("changeEndDateTime")
    this.setData({ 
      Endshow: false
     });
  },
  changeEndDateTimeColumn(e){
    // console.log("changeEndDateTimeColumn")
    var arr = this.data.Endvalue, dateArr = this.data.dateTimeArray;
    if(e.detail.column==1 || e.detail.column==2){
      arr[e.detail.column] = e.detail.value+2;
    }
    else{
      arr[e.detail.column] = e.detail.value;
    }
    dateArr[2] = dateTimePicker.getMonthDay(dateArr[0][arr[0]], dateArr[1][arr[1]]);
    let newtime = this.Timeformat(arr)
    this.setData({
      dateTimeArray: dateArr,
      Endvalue: arr,
      searchEndValue:newtime
    });
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
