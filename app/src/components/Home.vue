<template>
  <section class="section">
    <div class="container">
      <h1 class="title">タスク管理アプリ</h1>

      <div v-masonry transition-duration="0.2s" item-selector=".masonry-item" class="masonry-container">
        <div v-masonry-tile class="masonry-item"
          v-for="(category, index) in categories" :key="'category-' + index"
        >
          <div class="panel">
            <div :class="'panel-heading notification ' + category.class">
              <span class="has-text-weight-bold">{{category.title}}</span>
              <button class="button is-pulled-right" @click.prevent="toggleCategoryPanel(index)">
                <i :class="'fas ' + (category.open? 'fa-toggle-on': 'fa-toggle-off')"></i>
              </button>
              <button class="button is-pulled-right" @click.prevent="newTask(index)"><i class="fas fa-plus"></i></button>
            </div>
            <!-- 各タスクカードはドラッグ可能にする
              - v-model: vue.tasks[] 配列 と現在の状況を同期
              - group: グループ名を統一することで別タスクグループへのD&D可能に
            -->
            <!-- 各タスクカードは縦並びタイル化する -->
            <!-- ドラッグ前後の情報を確認するためタスクリストのindexをdata-groupに保持 -->
            <draggable v-model="tasks[index]" group="task_group" @end="onDragEnd"
              class="panel-block tile is-parent is-vertical" v-if="category.open"
              :data-group="index"
            >
              <div :class="'card tile is-child ' + (index == 3? 'is-disabled': '')" v-for="(task, t_index) in tasks[index]" :key="'task-' + index + '-' + t_index">
                <header class="card-header">
                  <!-- タスクタイトル、タスク編集系ボタン表示 -->
                  <span class="card-header-title">{{task.title}}</span>
                  <button class="card-header-title button is-info is-pulled-right" @click.prevent="showTask(task)"><i class="fas fa-eye"></i></button>
                  <button class="card-header-title button is-link is-pulled-right" @click.prevent="editTask(task)"><i class="fas fa-edit"></i></button>
                  <button class="card-header-title button is-danger is-pulled-right" @click.prevent="removeTask(index, t_index)"><i class="fas fa-trash"></i></button>
                </header>
                <footer class="card-footer">
                  <!-- 開始日表示 -->
                  <time :datetime="task.start_date" class="card-footer-item"><i class="fas fa-hourglass-start"></i>&nbsp;<span>{{task.start_date}}</span></time>
                  <!-- 完了タスク以外は締切日を表示 -->
                  <time v-if="index < 3" :datetime="task.limit_date" class="card-footer-item">
                    <i class="fas fa-hourglass-end"></i>&nbsp;<span>{{task.limit_date}}</span>
                  </time>
                  <!-- 完了タスクは完了日を表示 -->
                  <time v-else :datetime="task.end_date" class="card-footer-item">
                    <i class="fas fa-check"></i>&nbsp;<span>{{task.end_date}}</span>
                  </time>
                </footer>
              </div>
            </draggable>
          </div>
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
import moment from 'moment';

export default {
  data() {
    return {
      // カテゴリーリスト
      categories: [
        {
          title: '未着手', class: 'is-warning', open: true
        },
        {
          title: '実行中', class: 'is-primary', open: true
        },
        {
          title: '保留・確認中', class: 'is-info', open: true
        },
        {
          title: '完了', class: 'is-success', open: true
        },
      ],
      // タスクリスト
      tasks: [[], [], [], []],
      // タスク詳細表示用
      detail_dialog_flag: false,
      detail_task: {},
      // タスク編集用
      edit_dialog_flag: false,
      edit_task: {}
    };
  },

  methods: {
    // タスクリストを取得
    async getTasks() {
      const res = await axios.post('/api/get/tasks/', {
        csrf: document.getElementById('csrf').value
      });
      this.tasks = res.data;
    },

    // タスクリストを更新
    async putTasks() {
      const res = await axios.post('/api/put/tasks/', {
        csrf: document.getElementById('csrf').value,
        tasks: this.tasks
      });
    },

    // 新規タスク挿入
    newTask(category_index) {
      this.tasks[category_index].unshift({
        title: '', content: '', start_date: '', limit_date: '', end_date: ''
      });
    },

    // タスクリストの表示切り替え
    toggleCategoryPanel(category_index) {
      this.categories[category_index].open = !this.categories[category_index].open;
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
    removeTask(category_index, task_index) {
      this.$buefy.dialog.confirm({
        message: 'タスクを削除します<br>よろしいですか？',
        onConfirm: () => {
          this.tasks[category_index].splice(task_index, 1);
          this.putTasks(); // タスク状況更新
        }
      })
    },

    // ドラッグ終了時処理
    onDragEnd(evt) {
      // 完了タスク以外から完了タスクに移動したら、完了日（＝現在日時）セット
      const completed_index = 3;
      if (evt.from.dataset.group != completed_index && evt.to.dataset.group == completed_index) {
        this.tasks[completed_index][evt.newIndex].end_date = moment().format('YYYY-MM-DD HH:mm');
      }
      // 完了タスクから完了タスク以外に移動したら、完了日を削除
      if (evt.from.dataset.group == completed_index && evt.to.dataset.group != completed_index) {
        this.tasks[evt.to.dataset.group][evt.newIndex].end_date = '';
      }
      // タスクリスト更新
      this.putTasks();
      // Masonry再整列
      this.$redrawVueMasonry();
    }
  },

  async mounted() {
    // タスクリスト取得
    await this.getTasks();
    // Masonry再整列
    this.$redrawVueMasonry();
  }
}
</script>