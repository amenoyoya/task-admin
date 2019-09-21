<template>
  <section class="section">
    <div class="container">
      
      <div v-masonry transition-duration="1s" item-selector=".masonry-item" class="masonry-container">
        <div
          v-masonry-tile class="masonry-item"
          v-for="(category, index) in ['waiting', 'working', 'pending', 'completed']" :key="index"
        >
          <b-collapse :aria-id="todo[category].name" class="panel">
            <div class="panel-heading" :aria-controls="todo[category].name">
              <span class="has-text-weight-bold">{{todo[category].title}}</span>
              <button class="button is-pulled-right" @click.prevent="togglePanel(category)">
                <i :class="'fas ' + (todo[category].open? 'fa-toggle-on': 'fa-toggle-off')"></i>
              </button>
              <button class="button is-pulled-right" @click.prevent="newTask(category)"><i class="fas fa-plus"></i></button>
            </div>
            <div class="panel-block tile is-parent is-vertical" v-if="todo[category].open">
              <div class="card tile is-child" v-for="(task, t_index) in todo[category].tasks" :key="t_index">
                <header class="card-header">
                  <span class="card-header-title">{{task.title}}</span>
                  <button class="card-header-title button is-info is-pulled-right" @click.prevent="showTask(task)"><i class="fas fa-eye"></i></button>
                  <button class="card-header-title button is-link is-pulled-right" @click.prevent="editTask(task)"><i class="fas fa-edit"></i></button>
                  <button class="card-header-title button is-danger is-pulled-right" @click.prevent="removeTask(category, t_index)"><i class="fas fa-trash"></i></button>
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

    // 新規タスク挿入
    newTask(category) {
      this.todo[category].tasks.unshift({
        title: '', content: '', start_date: '', limit_date: '', end_date: ''
      });
    },

    // タスクリストの表示切り替え
    togglePanel(category) {
      this.todo[category].open = !this.todo[category].open;
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
    },

    // タスク削除
    removeTask(category, index) {
      this.$buefy.dialog.confirm({
        message: 'タスクを削除します<br>よろしいですか？',
        onConfirm: () => {
          this.todo[category].tasks.splice(index, 1);
          this.putTasks(); // タスク状況更新
        }
      })
    },
  },

  async mounted() {
    // TODOデータ取得
    await this.getTasks();
    // Masonryで再整列
    this.$redrawVueMasonry();
  }
}
</script>