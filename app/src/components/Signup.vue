<template>
  <div class="container">
    <h1 class="title">ユーザー登録</h1>
    
    <transition
      name="custom-classes-transition"
      enter-active-class="animated fadeInUp"
      leave-active-class="animated fadeOutDown"
    >
      <div class="notification is-success" v-if="info !== ''">{{ info }}</div>
      <div class="notification is-warning" v-if="warning !== ''">{{ warning }}</div>
      <div class="notification is-danger" v-if="error !== ''">{{ error }}</div>
    </transition>

    <vee-observer v-slot="{valid}">
      <form @submit.prevent="signup">
        <vee-validator class="field" rules="required|alpha_num|max:15" v-slot="{errors}" name="ユーザー名">
          <label for="username" class="label">Username</label>
          <div class="control">
            <input name="username" class="input" type="text" v-model="username" placeholder="admin">
          </div>
          <p class="is-size-7">※ユーザー名は15文字以内の半角英数字を指定してください</p>
          <transition
            name="custom-classes-transition"
            enter-active-class="animated fadeInLeft"
            leave-active-class="animated fadeOutRight"
          >
            <p class="notification is-warning" v-if="disabled = (errors.length > 0)">{{ errors[0] }}</p>
          </transition>
        </vee-validator>

        <vee-validator class="field" rules="required|max:30" v-slot="{errors}" name="パスワード">
          <label for="password" class="label">Password</label>
          <div class="control">
            <input id="password" class="input" type="password" v-model="password">
          </div>
          <p class="is-size-7">※パスワードは30文字以内で指定してください</p>
          <transition
            name="custom-classes-transition"
            enter-active-class="animated fadeInLeft"
            leave-active-class="animated fadeOutRight"
          >
            <p class="notification is-warning" v-if="disabled = (errors.length > 0)">{{ errors[0] }}</p>
          </transition>
        </vee-validator>

        <div>
          <button class="button is-link" type="submit" :disabled="!valid">Sign up</button>
        </div>
      </form>
    </vee-observer>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      info: '',
      warning: '',
      error: '',
      disabled: true,
      username: '',
      password: ''
    };
  },
  methods: {
    signup() {
      this.info = '', this.warning = '', this.error = '';
      axios.post('/api/signup/', {
        csrf: document.getElementById('csrf').value, username: this.username, password: this.password
      })
        .then((res) => {
          if (res.data.reg) {
            this.info = res.data.message;
          } else {
            this.warning = res.data.message;
          }
        })
        .catch((err) => {
          this.error = 'サーバーエラー ' + err.response.status + ': ' + err.response.statusText;
        });
    }
  }
}
</script>
