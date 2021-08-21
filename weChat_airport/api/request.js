function request(method, url, data) {
  //返回一个Promise对象
  return new Promise(function (resolve, reject) {
    // ----------   添加loding   ----------
    wx.showLoading({
      title: '加载中',
    })
    // ------------------------------------
    wx.request({
      url: url,
      method: method,
      data: data,
      header: {
        'content-type': 'application/json',
        'Authorization': 'APPCODE f6e5fe019ad94eb8b9ca5ed53dd9d48e',
        'apicode': 'edc23e7ffda74a42ba8c9c208ef161f3'
      },
      success: function (res) {
        // console.log(res)
        if (res) {

          // ----------   隐藏loding   ----------
          setTimeout(function () {
            wx.hideLoading()
          }, 500)
          // ------------------------------------

          // ----------   返回数据处理   ----------
          if (res.data) {
            resolve(res.data);
          } else {
            resolve(res)
          }
          // ------------------------------------

        } else {

          // ----------   出现异常   ----------
          console.error("返回结果出现异常：", res)
          // ------------------------------------

        }
      },
      fail: function (res) {

        // ----------   抛出异常   ----------
        console.error("请求超时：", res)
        // ------------------------------------

      }
    });
  });
}

// get请求
function get(url, data = {}) {
  return request("GET", url, data);
}

// post请求
function post(url, data = {}) {
  return request("POST", url, data);
}

module.exports = {
  get: get,
  post: post
}
