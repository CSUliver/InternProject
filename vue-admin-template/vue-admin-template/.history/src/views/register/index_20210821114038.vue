<template>
  <div class="login-container">

    <el-row>
      <el-col :xs="24" :sm="24" :md="12" :lg="16" :xl="16">
        <div style="color: transparent">占位符</div>
      </el-col>
      <el-col :xs="24" :sm="24" :md="12" :lg="8" :xl="8">
        <el-form
          ref="form"
          :model="form"
          :rules="rules"
          class="login-form"
          label-position="left"
        >
          <div class="title">hello !</div>
          <div class="title-tips">欢迎注册{{ title }}！</div>
          <el-form-item style="margin-top: 40px" prop="username">
            <span class="svg-container svg-container-admin">
              <vab-icon :icon="['fas', 'user']" />
            </span>
            <el-input
              v-model.trim="form.username"
              v-focus
              placeholder="请输入用户名"
              tabindex="1"
              type="text"
            />
          </el-form-item>
          <el-form-item prop="password">
            <span class="svg-container">
              <vab-icon :icon="['fas', 'lock']" />
            </span>
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
              <vab-icon :icon="['fas', 'eye-slash']"></vab-icon>
            </span>
            <span v-else class="show-password" @click="handlePassword">
              <vab-icon :icon="['fas', 'eye']"></vab-icon>
            </span>
          </el-form-item>

          <el-form-item prop="person_type">
          <span class="svg-container svg-container-admin">
              <vab-icon :icon="['fas', 'user']" />
            </span>
            <!-- <el-input
              v-model.trim="form.person_type"
              v-focus
              placeholder="请输入用户名"
              tabindex="1"
              type="text"
            /> -->
            <el-radio-group v-model="form.person_type" size="medium">
            <el-radio-button border label="admin">机场管理员</el-radio-button>
            <el-radio-button border label="passenger">旅客</el-radio-button>
            <el-radio-button border label="airport">机场工作人员</el-radio-button>
            <el-radio-button border label="flight">机组人员</el-radio-button>
          </el-radio-group>
          </el-form-item>

          <router-link to="/login">
          <el-button
            :loading="loading"
            class="login-btn"
            type="primary"
          >
            去登录
          </el-button>
            <!-- <div style="margin-top: 20px">注册</div> -->
          </router-link>
          <el-button
            :loading="loading"
            class="login-btn"
            type="primary"
            @click="addUserInfo"
          >
            注册
          </el-button>
          <!-- <router-link to="/register">
            <div style="margin-top: 20px">注册</div>
          </router-link> -->
        </el-form>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import { validUsername } from "@/utils/validate";

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
      addUserInfo:function(){
      // 发起请求：新增用户-如果不涉及图片
      // request({url:"/users/users/",method:"post",data:this.adduserform}).then(res=>{
      //   // 请求成功后的逻辑处理
      // })
      // 发起请求：新增用户-涉及到文件上传（二进制流）
      /*
        FormData:用键值对模拟表单控件，用form表单控件中的name以及value值组成一个querystring
        作用：一般用来异步上传二进制文件
      */
      var form = new FormData()
      form.append('username',this.form.username)
      form.append('password',this.form.password)
      form.append('person_type',this.form.person_type)
      request({
        url:"/users/users/",
        method:"post",
        headers:{"Content-Type":"multipart/form-data"},
        data:form
      }).then(res=>{
        // 请求成功后的逻辑处理
        this.$message({
          message: '恭喜你，注册成功',
          type: 'success'
        });
      }).catch(error=>{
        // 请求失败的逻辑处理
        console.log(error);
        this.$message({
          message: '注册失败',
          type: 'warning'
        });
   
      })
      // .finally(()=>{
      //   this.addUserFormVisible = false;
      // })
    },
    handleRegister() {
        this.$refs.form.validate((valid) => {
          if (valid) {
            this.addUserInfo()
            // this.loading = true;
            // this.$store
            //   .dispatch("user/register", this.form)
            //   .then(() => {
            //     const routerPath =
            //       this.redirect === "/404" || this.redirect === "/401"
            //         ? "/"
            //         : this.redirect;
            //     this.$router.push(routerPath).catch(() => {});
            //     this.loading = false;
            //   })
            //   .catch(() => {
            //     this.loading = false;
            //   });
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
    height: 100vh;
    // background: url("~@/assets/login_images/background.jpg") center center fixed
    //   no-repeat;
    background: url("~@/assets/login_images/6.jpg") center center fixed
      no-repeat;
    background-size: cover;

    .title {
      font-size: 54px;
      font-weight: 500;
      color: rgba(14, 18, 26, 1);
    }

    .title-tips {
      margin-top: 29px;
      font-size: 26px;
      font-weight: 400;
      color: rgba(14, 18, 26, 1);
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .login-btn {
      display: inherit;
      width: 220px;
      height: 60px;
      margin-top: 5px;
      border: 0;

      &:hover {
        opacity: 0.9;
      }
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

    .tips {
      margin-bottom: 10px;
      font-size:small;
      color: red;

      span {
        &:first-of-type {
          margin-right: 16px;
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

    .svg-container {
      position: absolute;
      top: 14px;
      left: 15px;
      z-index: -1;
      font-size: 16px;
      color: #d7dee3;
      cursor: pointer;
      user-select: none;
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

    ::v-deep {
      .el-form-item {
        padding-right: 0;
        margin: 20px 0;
        color: #454545;
        background: transparent;
        border: 1px solid transparent;
        border-radius: 2px;

        &__content {
          min-height: 100px;
          line-height: 110%;
        }

        &__error {
          position: absolute;
          top: 100%;
          left: 18px;
          font-size: small;
          line-height: 18px;
          color: red;
        }
      }

      .el-input {
        box-sizing: border-box;

        input {
          height: 58px;
          padding-left: 45px;
          font-size: medium;
          line-height: 58px;
          color: blue;
          background: #f6f4fc;
          border: 0;
          caret-color: green;
        }
      }
    }
  }
</style>
