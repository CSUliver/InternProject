import request from './request.js';

const api = {
  // 获取疫情数据
  getMessage() { return request.get("https://ncovdata.market.alicloudapi.com/ncov/cityDiseaseInfoWithTrend"); },
  // 获取疫情地图数据
  getOnsInfo() { return request.get("https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5") },
  // 获取疫情谣言
  identifyRumor() { return request.get("https://api.yonyoucloud.com/apis/dst/ncov/identifyRumor") },
  // 疫情动态播报
  query(data) { return request.get("https://wuhan.wbjiang.cn/api/timeline", { 'pageNo': data.pageNo, 'pageSize': data.pageSize }) },
  // 疾病知识
  wiki(data) { return request.get("https://wuhan.wbjiang.cn/api/wiki") }
}

export default api;
