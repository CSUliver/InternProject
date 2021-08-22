<template>
  <div class="login-container">
    <el-row>
      <el-form
        ref="form"
        :model="form"
        :rules="rules"
        class="login-form"
        label-position="left"
      >
        <div class="container">
          <div class="title-tips">欢迎注册</div>
          <el-form-item style="margin-top: 20px" prop="username">
            <el-input
              v-model.trim="form.username"
              v-focus
              placeholder="请输入用户名"
              tabindex="1"
              type="text"
            />
          </el-form-item>
          <el-form-item prop="password">
            <el-input
              :key="passwordType"
              ref="password"
              v-model.trim="form.password"
              :type="passwordType"
              tabindex="2"
              placeholder="请输入密码"
              @keyup.enter.native="handleRegister"
            />
            <span
              v-if="passwordType === 'password'"
              class="show-password"
              @click="handlePassword"
            >
              <!-- <vab-icon :icon="['fas', 'eye-slash']"></vab-icon> -->
            </span>
            <span v-else class="show-password" @click="handlePassword">
              <!-- <vab-icon :icon="['fas', 'eye']"></vab-icon> -->
            </span>
          </el-form-item>

          <el-form-item prop="person_type">
            <span class="svg-container svg-container-admin">
              <!-- <vab-icon :icon="['fas', 'user']" /> -->
            </span>
            <el-radio-group class="form-container" v-model="form.person_type" size="medium">
              <el-radio-button style="margin-left:6px;width:49%" border label="admin">机场管理人员</el-radio-button>
              <el-radio-button style="width: 100px;" border label="passenger">旅客人员</el-radio-button>
              <el-radio-button style="margin-left:6px;width:49%" border label="airport"
                >机场工作人员</el-radio-button
              >
              <el-radio-button style="width: 100px;" border label="flight">机组人员</el-radio-button>
            </el-radio-group>
          </el-form-item>
          <el-button
            :loading="loading"
            class="login-btn"
            type="primary"
            @click="handleRegister"
          >
            注册
          </el-button>

          <router-link to="/login">
            <div class="loginb-container">
              <div style="margin-top: 10px; font-size: 10px">
                账号注册成功啦？
              </div>
              <div
                style="
                  margin-top: 10px;
                  color: rgb(11, 115, 252);
                  font-size: 10px;
                "
              >
                点我返回登录哦
              </div>
            </div>
          </router-link>
        </div>
      </el-form>
    </el-row>
  </div>
</template>

<script>
import { validUsername } from "@/utils/validate";
import request from "@/utils/request";
export default {
  name: "Login",
  directives: {
    focus: {
      inserted(el) {
        el.querySelector("input").focus();
      },
    },
  },
  data() {
    const validateusername = (rule, value, callback) => {
      if ("" == value) {
        callback(new Error("用户名不能为空"));
      } else {
        callback();
      }
    };
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error("密码不能少于6位"));
      } else {
        callback();
      }
    };
    return {
      nodeEnv: process.env.NODE_ENV,
      title: this.$baseTitle,
      form: {
        username: "",
        password: "",
      },
      rules: {
        username: [
          {
            required: true,
            trigger: "blur",
            validator: validateusername,
          },
        ],
        password: [
          {
            required: true,
            trigger: "blur",
            validator: validatePassword,
          },
        ],
      },
      loading: false,
      passwordType: "password",
      redirect: undefined,
    };
  },
  watch: {
    $route: {
      handler(route) {
        this.redirect = (route.query && route.query.redirect) || "/";
      },
      immediate: true,
    },
  },
  created() {
    document.body.style.overflow = "hidden";
  },
  beforeDestroy() {
    document.body.style.overflow = "auto";
  },
  mounted() {
    this.form.username = "";
    this.form.password = "";
    // setTimeout(() => {
    //   this.handleLogin();
    // }, 300000);
  },
  methods: {
    handlePassword() {
      this.passwordType === "password"
        ? (this.passwordType = "")
        : (this.passwordType = "password");
      this.$nextTick(() => {
        this.$refs.password.focus();
      });
    },
    addUserInfo: function () {
      // 发起请求：新增用户-如果不涉及图片
      // request({url:"/users/users/",method:"post",data:this.adduserform}).then(res=>{
      //   // 请求成功后的逻辑处理
      // })
      // 发起请求：新增用户-涉及到文件上传（二进制流）
      /*
        FormData:用键值对模拟表单控件，用form表单控件中的name以及value值组成一个querystring
        作用：一般用来异步上传二进制文件
      */
      var form = new FormData();
      form.append("username", this.form.username);
      form.append("password", this.form.password);
      form.append("person_type", this.form.person_type);
      request({
        url: "/users/users/",
        method: "post",
        headers: { "Content-Type": "multipart/form-data" },
        data: form,
      })
        .then((res) => {
          // 请求成功后的逻辑处理
          this.$message({
            message: "恭喜你，注册成功",
            type: "success",
          });
        })
        .catch((error) => {
          // 请求失败的逻辑处理
          console.log(error);
          this.$message({
            message: "注册失败",
            type: "warning",
          });
        });
      // .finally(()=>{
      //   this.addUserFormVisible = false;
      // })
    },
    handleRegister() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          this.addUserInfo();
        } else {
          return false;
        }
      });
    },
  },
};
</script>

<style lang="scss" scoped>
  .login-container {
    height: 100%;
    // background: url("~@/assets/login_images/background.jpg") center center fixed
    //   no-repeat;
    background: url("~@/assets/login_images/6.jpg") center center fixed no-repeat;
    background-size: cover;
  }

  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 332px;
    height: 400px;
    background: rgba(230, 227, 227, 0.4);
    border-radius: 2px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    margin-top: 200px;
    margin-left: 1060px;
  }

  .loginb-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin-bottom: 6px;
  }

  .form-container{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
  }

  .title-tips {
    margin-top: 10px;
    font-family: "PingFang SC";
    font-size: 20px;
    font-weight: bold;
    color: rgb(3, 3, 3);
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .login-btn {
    width: 120px;
    height: 40px;
    margin-top: 5px;
    border: 0;

    &:hover {
      opacity: 0.9;
    }
  }

  .el-form-item.is-error.is-required {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

  .el-form.login-form.el-form--label-left{
    margin: 2px;
  }

  .login-form {
    position: relative;
    max-width: 100%;
    margin: calc((100vh - 425px) / 2) 10% 10%;
    overflow: hidden;

    .forget-password {
      width: 100%;
      margin-top: 40px;
      text-align: left;

      .forget-pass {
        width: 129px;
        height: 19px;
        font-size: 20px;
        font-weight: 400;
        color: rgba(92, 102, 240, 1);
      }
    }
  }

  .title-container {
    position: relative;

    .title {
      margin: 0 auto 40px auto;
      font-size: 34px;
      font-weight: bold;
      color: blue;
      text-align: center;
    }
  }

  .show-password {
    position: absolute;
    top: 14px;
    right: 25px;
    font-size: 16px;
    color: #d7dee3;
    cursor: pointer;
    user-select: none;
  }
</style>
