import Vue from 'vue'; // Vue を使う
import App from './App'; // App.vue を読み込む

// IE11/Safari9用のpolyfill
// babel-polyfill を import するだけで IE11/Safari9 に対応した JavaScript にトランスコンパイルされる
import 'babel-polyfill';

// Buefy
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
Vue.use(Buefy);

// masonry
import {VueMasonryPlugin} from 'vue-masonry';
Vue.use(VueMasonryPlugin);

// CtkDatetimePicker
import VueCtkDateTimePicker from 'vue-ctk-date-time-picker';
import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css';
Vue.component('ctk-datetime-picker', VueCtkDateTimePicker);

// QuillEditor
import VueQuillEditor from 'vue-quill-editor';
import 'quill/dist/quill.core.css';
import 'quill/dist/quill.snow.css';
import 'quill/dist/quill.bubble.css';
Vue.use(VueQuillEditor);

// VueDraggable
import VueDraggable from 'vuedraggable';
Vue.component('draggable', VueDraggable);

// VueDraggable は値を書き換える系のコンポーネントのため、コンソールに警告が出る
// 開発ツールがうるさくなるのが嫌な場合は Vue の警告を無視する
Vue.config.warnHandler = (msg, vm, trace) => {
  msg = null;
  vm = null;
  trace = null;
}

// Cardコンポーネントを <task-card> として登録する
import Card from './components/Card';
Vue.component('task-card', Card);

// Panelコンポーネントを <task-panel> として登録する
import Panel from './components/Panel';
Vue.component('task-panel', Panel);

/**
 * public/api.js で定義したAPIのラッピングメソッド
 * => 同期処理関数（readFileSync, writeFileSync）を使っているため async, await を使って呼び出す
 * => 全てのコンポーネントから呼び出せるように mixin でグローバルメソッド化
 */
Vue.mixin({
  data() {
    return {
      // Panelコンポーネントに渡す task データ配列: @see components/Card.vue, components/Panel.vue
      task_lists: [
        [ /*未着手*/ ], [ /*実行中*/ ], [ /*確認・保留中*/ ], [ /*完了*/ ]
      ],
    }
  },
  methods: {
    // タスクリストを読み込み、Masonry再整列実行
    async loadTasksAndRedrawMasonry() {
      this.task_lists = await loadTasks()
      // DOM更新後にMasonryによる整列を実行
      this.$nextTick(function() {
        this.$redrawVueMasonry()
      })
    },

    // タスクリストを保存し、Masonry再整列実行
    async saveTasksAndRedrawMasonry() {
      // DOM更新後にMasonryによる整列を実行
      this.$nextTick(function() {
        this.$redrawVueMasonry()
      })
      await saveTasks(this.task_lists)
    }
  }
})

new Vue({
  el: '#app', // Vueでマウントする要素
  render: h => h(App), // App.vue をレンダリング
});
