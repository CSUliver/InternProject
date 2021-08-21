<template>
  <div class="login-container">
    <div class="title-tips">机场人员流动监测系统</div>

    <div class="left-container">
      <el-form
        ref="form"
        :model="form"
        :rules="rules"
        class="login-form"
        label-position="left"
      >
        <div class="container">
          <div class="title-user">账号登录</div>
          <el-form-item style="margin-top: 10px" prop="username">
            <div class="el-icon-user"></div>
            <el-input
              v-model.trim="form.username"
              v-focus
              placeholder="请输入用户名"
              tabindex="1"
              type="text"
            />
          </el-form-item>
          <el-form-item prop="password">
            <div class="el-icon-lock"></div>
            <el-input
              :key="passwordType"
              ref="password"
              v-model.trim="form.password"
              :type="passwordType"
              tabindex="2"
              placeholder="请输入密码"
              @keyup.enter.native="handleLogin"
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
          <el-button
            :loading="loading"
            class="login-btn"
            type="primary"
            @click="handleLogin"
          >
            登录
          </el-button>
          <router-link to="/register">
            <div class="register-container">
              <div style="margin-top: 10px;font-size: 10px;">还没有账号？</div>
              <div style="margin-top: 10px;color:rgb(11, 115, 252);font-size: 10px;">快点我注册一个叭</div>
            </div>
          </router-link>
        </div>
      </el-form>
    </div>
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
    setTimeout(() => {
      this.handleLogin();
    }, 300000);
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
    handleLogin() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          this.loading = true;
          this.$store
            .dispatch("user/login", this.form)
            .then(() => {
              const routerPath =
                this.redirect === "/404" || this.redirect === "/401"
                  ? "/"
                  : this.redirect;
              this.$router.push(routerPath).catch(() => {});
              this.loading = false;
            })
            .catch(() => {
              this.loading = false;
            });
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
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  height: 100vh;
  // background: url("~@/assets/login_images/background.jpg") center center fixed
  //   no-repeat;
  background: url("~@/assets/login_images/3.png") center center fixed no-repeat;
  background-size: cover;
  }

  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 332px;
    height: 360px;
    background: rgba(38, 41, 63, 0.3);
    border-radius: 2px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    margin-bottom: 160px;
  }

  .register-container{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    margin-bottom: 6px;
  }

  .left-container {
    width: 400px;
  }

  .title-tips {
    margin-bottom: 220px;
    margin-right: 400px;
    font-family: "PingFang SC";
    font-size: 60px;
    font-weight: bold;
    color: rgb(255, 255, 255);
    text-overflow: ellipsis;
    white-space: nowrap;
  }

    .title-user {
    margin-top: 10px;
    font-family: "PingFang SC";
    font-size: 20px;
    font-weight: bold;
    color: rgb(251, 253, 255);
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
  // ::v-deep {
  //   .el-form-item {
  //     display: flex;
  //     flex-direction: row;
  //     justify-content: center;
  //     align-items: center;
  //     border: none;
  //     border-bottom: 1px solid rgb(255, 253, 253);
  //     border-radius: 2px;

  //     // &__content {
  //     //   min-height: 100px;
  //     //   line-height: 110%;
  //     // }

  //     &__error {
  //       position: absolute;
  //       top: 100%;
  //       left: 18px;
  //       font-size: small;
  //       line-height: 18px;
  //       color: rgb(5, 5, 5);
  //     }
  //   }

  //   .el-input {
  //     // box-sizing: border-box;
  //     border: none;
  //     border-bottom: 1px solid rgb(255, 253, 253);

  //     &_input {
  //       height: 58px;
  //       padding-left: 45px;
  //       font-size: medium;
  //       line-height: 58px;
  //       // caret-color: green;
  //     }
  //   }
  // }

</style>