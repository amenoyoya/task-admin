<template>
  <div class="container">
    <h1 class="title">ログイン画面</h1>
    
    <transition
      name="custom-classes-transition"
      enter-active-class="animated fadeInUp"
      leave-active-class="animated fadeOutDown"
    >
      <div class="notification is-warning" v-if="warning !== ''">{{ warning }}</div>
      <div class="notification is-danger" v-if="error !== ''">{{ error }}</div>
    </transition>
    
    <form @submit.prevent="login">
      <div class="field">
        <label for="username" class="label">Username</label>
        <div class="control">
          <input id="username" class="input" type="text" v-model="username">
        </div>
      </div>
      <div class="field">
        <label for="password" class="label">Password</label>
        <div class="control">
          <input id="password" class="input" type="password" v-model="password">
        </div>
      </div>
      <div>
        <button class="button is-link" type="submit">Login</button>
      </div>
    </form>
    
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      warning: '',
      error: '',
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      this.warning = '', this.error = '';
      axios.post(this.$store.state.config.endpoints.login, {
        csrf: document.getElementById('csrf').value, username: this.username, password: this.password
      })
        .then((res) => {
          if (res.data.login) {
            this.$store.commit('authenticate', res.data);
            console.log(this.$route.query.redirect || '/dashboard');
            this.$router.push(this.$route.query.redirect || '/dashboard');
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
