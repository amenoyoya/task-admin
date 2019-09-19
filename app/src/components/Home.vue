<template>
  <section class="section">
    <div class="container">
      <div class="tile is-ancestor">
        <div class="tile is-3" v-for="category in todo">
          <div class="card" v-for="c in category">
            <header class="card-header">
              <p class="card-header-title">{{c.title}}</p>
              <time v-if="c.limit_date != ''" :datetime="c.limit_date" class="card-header-title">〜<span>{{c.limit_date}}</span></time>
            </header>
            <div class="card-content">
              <div class="content" v-html="c.content"></div>
            </div>
            <footer class="card-footer">
              <time :datetime="c.start_date" class="card-footer-item">開始日: <span>{{c.start_date}}</span></time>
              <time :datetime="c.end_date" class="card-footer-item">完了日: <span>{{c.end_date}}</span></time>
            </footer>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      todo: {
        waiting: [],
        working: [],
        pending: [],
        completed: [],
      }
    };
  },

  async mounted() {
    // TODOデータ取得
    const res = await axios.get('/static/data.json');
    this.todo.waiting = res.data.waiting;
    this.todo.working = res.data.working;
    this.todo.pending = res.data.pending;
    this.todo.completed = res.data.completed;
  }
}
</script>