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
              <div class="card" v-for="(task, t_index) in category.tasks" :key="t_index" style="width: 100%;">
                <header class="card-header">
                  <span class="card-header-title">{{task.title}}</span>
                  <button class="card-header-title button is-info is-pulled-right" @click.prevent="showTask(task)"><i class="fas fa-comment"></i></button>
                  <button class="card-header-title button is-link is-pulled-right" @click.prevent="editTask(task)"><i class="fas fa-edit"></i></button>
                  <button class="card-header-title button is-danger is-pulled-right"><i class="fas fa-trash"></i></button>
                </header>
                <footer class="card-footer">
                  <time :datetime="task.start_date" class="card-footer-item"><i class="fas fa-hourglass-start"></i>&nbsp;<span>{{task.start_date}}</span></time>
                  <time :datetime="task.limit_date" class="card-footer-item"><i class="fas fa-hourglass-end"></i>&nbsp;<span>{{task.limit_date}}</span></time>
                </footer>
              </div>
            </div>
          </b-collapse>
        </div>
      </div>

      <b-modal :active.sync="detail_dialog_flag" has-modal-card>
        <detail-dialog :detail_task="detail_task"></detail-dialog>
      </b-modal>

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
      // TODOタスク
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
      // タスク詳細表示用
      detail_dialog_flag: false,
      detail_task: {},
      // タスク編集用
      edit_dialog_flag: false,
      edit_task: {}
    };
  },

  methods: {
    showTask(task) {
      this.detail_task = task;
      this.detail_dialog_flag = true;
    },

    editTask(task) {
      this.edit_task = task;
      this.edit_dialog_flag = true;
    }
  },

  async mounted() {
    // TODOデータ取得
    const res = await axios.post('/api/get/todo/', {
      csrf: document.getElementById('csrf').value
    });
    this.todo.waiting.tasks = res.data.waiting;
    this.todo.working.tasks = res.data.working;
    this.todo.pending.tasks = res.data.pending;
    this.todo.completed.tasks = res.data.completed;
  }
}
</script>