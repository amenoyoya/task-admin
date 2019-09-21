<template>
  <section class="section">
    <div class="container">
      
      <div class="tile is-ancestor">
        <div class="tile is-3" v-for="(category, index) in ['waiting', 'working', 'pending', 'completed']" :key="index">
          <b-collapse :aria-id="todo[category].name" class="panel" :open.sync="todo[category].open">
            <div slot="trigger" class="panel-heading" role="button" :aria-controls="todo[category].name">
              <strong>{{todo[category].title}}</strong>
            </div>
            <div class="panel-block">
              <div class="card" v-for="(task, t_index) in todo[category].tasks" :key="t_index">
                <header class="card-header">
                  <span class="card-header-title">{{task.title}}</span>
                  <button class="card-header-title button is-info is-pulled-right" @click.prevent="showTask(task)"><i class="fas fa-eye"></i></button>
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

      <b-modal :active.sync="detail_dialog_flag">
        <detail-dialog :detail_task="detail_task"></detail-dialog>
      </b-modal>

      <b-modal :active.sync="edit_dialog_flag" has-modal-card>
        <edit-dialog :edit_task="edit_task" @putTasks="putTasks"></edit-dialog>
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
    // TODOリストを取得
    async getTasks() {
      const res = await axios.post('/api/get/todo/', {
        csrf: document.getElementById('csrf').value
      });
      this.todo = res.data;
    },

    // TODOリストを更新
    async putTasks() {
      const res = await axios.post('/api/put/todo/', {
        csrf: document.getElementById('csrf').value,
        todo: this.todo
      });
      console.log(res.data);
    },

    // 指定タスクの詳細表示
    showTask(task) {
      this.detail_task = task;
      this.detail_dialog_flag = true;
    },
    
    // 指定タスクの編集
    editTask(task) {
      this.edit_task = task;
      this.edit_dialog_flag = true;
    }
  },

  mounted() {
    // TODOデータ取得
    this.getTasks();
  }
}
</script>