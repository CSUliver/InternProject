<template>
  <div>
      socket is loading...
      <echartsline :linedata="tlinedata"></echartsline>
  </div>
</template>
 
<script>
import Stomp from 'stompjs'
import { MQ_SERVICE, MQ_USERNAME, MQ_PASSWORD } from '../../config/linkparams.js'
import echartsline from '../../components/EchartsComponents/EchartsLine.vue'
export default {
  name: 'entry',
  components:{
    echartsline
  },
  data () {
    return {
      client: Stomp.client(MQ_SERVICE),
      tlinedata: {
        title: "温度折线图",
        legend: "温度",
        xdata: [],
        ydata: [],
        type: "line",
        color: "#ffb6b9",
      }
    }
  },
  created () {
    this.connect()
  },
  methods: {
    onConnected: function (frame) {
      console.log('Connected: ' + frame)
      var topic = '/topic/SampleTopic'
      //读取数据的位置
      this.client.subscribe(topic, this.responseCallback, this.onFailed)
    },
    onFailed: function (frame) {
      console.log('Failed: ' + frame)
    },
    responseCallback: function (frame) {
      console.log('responseCallback msg=>' + frame.body)
      console.log('------')
      //从消息队列中获取实时数据逻辑处理,时间放入xdata，value放入ydata
      //console.log(typeof frame)
      var data =JSON.parse(frame.body)
      this.tlinedata.xdata.push(data.mtime);
      this.tlinedata.ydata.push(data.values);
    },
    connect: function () {
      var headers = {
        'login': MQ_USERNAME,
        'passcode': MQ_PASSWORD
      }
      this.client.connect(headers, this.onConnected, this.onFailed)
    }
  }
}
</script>