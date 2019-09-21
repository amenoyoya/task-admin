<template>
  <section class="section">
    <div class="container">
      <div class="tile is-ancestor">
        <div class="tile is-3" v-for="(category, index) in todo" :key="index">
          <b-collapse :aria-id="category.name" class="panel" :open.sync="category.open">
            <div slot="trigger" class="panel-heading" role="button" :aria-controls="category.name">
              <strong>{{category.title}}</strong>
            </div>
            <div class="panel-block">
              <a class="card" v-for="(task, t_index) in category.tasks" :key="t_index" @click.prevent="editTask(task)">
                <header class="card-header">
                  <p class="card-header-title">{{task.title}}</p>
                  <time v-if="task.limit_date != ''" :datetime="task.limit_date" class="card-header-title">〜<span>{{task.limit_date}}</span></time>
                </header>
                <div class="card-content">
                  <div class="content" v-html="task.content"></div>
                </div>
                <footer class="card-footer">
                  <time :datetime="task.start_date" class="card-footer-item">開始日: <span>{{task.start_date}}</span></time>
                  <time :datetime="task.end_date" class="card-footer-item">完了日: <span>{{task.end_date}}</span></time>
                </footer>
              </a>
            </div>
          </b-collapse>
        </div>
      </div>
      <b-modal :active.sync="edit_dialog_flag" has-modal-card>
        <edit-dialog :edit_task="edit_task"></edit-dialog>
      </b-modal>
    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      todo: {
        waiting: {
          name: 'waiting_task', title: '未着手', open: true, tasks: [],
        },
        working: {
          name: 'working_task', title: '実行中', open: true, tasks: [],
        },
        pending: {
          name: 'pending_task', title: '保留・確認中', open: true, tasks: [],
        },
        completed: {
          name: 'completed_task', title: '完了', open: true, tasks: [],
        }
      },
      edit_dialog_flag: false,
      edit_task: {
        title: '', content: ''
      }
    };
  },

  methods: {
    editTask(task) {
      this.edit_task = task;
      this.edit_dialog_flag = true;
    }
  },

  async mounted() {
    // TODOデータ取得
    const res = await axios.get('/static/data.json');
    this.todo.waiting.tasks = res.data.waiting;
    this.todo.working.tasks = res.data.working;
    this.todo.pending.tasks = res.data.pending;
    this.todo.completed.tasks = res.data.completed;
  }
}
</script>