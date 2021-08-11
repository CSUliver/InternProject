<template>
  <div class="app-container">
    <echartsline :linedata="tlinedata"></echartsline>
    <echartsline :linedata="slinedata"></echartsline>
    <echartsline></echartsline>
  </div>
  
</template>

<script>
import echartsline from "../../components/EchartsComponents/EchartsLine.vue"
export default {
  //应用组件
  components:{
    echartsline,
  },
  data(){
    return{
      tlinedata:{
        title:"温度折线图",
        legend:"温度",
        xdata:["周一","周二","周三","周四","周五"],
        ydata:[23,26,19,30,29],
        type:"line",
        color:"#ffb6b9",
      },
      slinedata:{
        title:"湿度折线图",
        legend:"湿度",
        xdata:["周一","周二","周三","周四","周五"],
        ydata:[23,26,19,30,29],
        type:"line",
        color:"#bbded6",
      }
    }
  }

}
</script>

<style scoped>
.line{
  text-align: center;
}
</style> 


