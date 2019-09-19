<template>
  <div>
    <nav-bar></nav-bar>
    <section class="section">
      <router-view></router-view>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  async mounted() {
    // APIルートからサーバー設定を取得
    const res = await axios.post('/api/', {csrf: document.getElementById('csrf').value});

    this.$store.commit('configure', res.data); // Storeに設定保存
    if (this.$route.query.redirect) {
      // redirect先がクエリに指定されているならリダイレクト
      this.$router.push(this.$route.query.redirect);
    } else {
      this.$router.push('/markdown/');
    }
  }
}
</script>