<template>
  <div :class="'card ' + getTaskClass()">
    <header class="card-header">
      <!-- タスクタイトル、タスク編集系ボタン表示 -->
      <span class="card-header-title">{{ task.title }}</span>
      <button class="card-header-title button is-info is-pulled-right" @click.prevent="onShow"><i class="fas fa-eye"></i></button>
      <button class="card-header-title button is-link is-pulled-right" @click.prevent="onEdit"><i class="fas fa-edit"></i></button>
      <button class="card-header-title button is-danger is-pulled-right" @click.prevent="onRemove"><i class="fas fa-trash"></i></button>
    </header>
    <footer class="card-footer">
      <!-- 開始日表示 -->
      <time :datetime="task.start_date" class="card-footer-item">
        <i class="fas fa-hourglass-start"></i>&nbsp;<span>{{ displayDatetime(task.start_date) }}</span>
      </time>
      <!-- 完了タスク以外は締切日を表示 -->
      <time v-if="!task.end_date" :datetime="task.limit_date" class="card-footer-item">
        <i class="fas fa-hourglass-end"></i>&nbsp;<span>{{ displayDatetime(task.limit_date) }}</span>
      </time>
      <!-- 完了タスクは完了日を表示 -->
      <time v-else :datetime="task.end_date" class="card-footer-item ">
        <i class="fas fa-check"></i>&nbsp;<span>{{ displayDatetime(task.end_date) }}</span>
      </time>
    </footer>
  </div>
</template>

<script>
import moment from 'moment'
import EditDialog from './EditDialog'
import DetailDialog from './DetailDialog'

/**
 * props として以下の値を親コンポーネントから受け取る
 * - task {
 *     title <string>:      タスク名
 *     content <string>:    内容
 *     start_date <string>: 開始日
 *     limit_date <string>: 締切日
 *     end_date <string>:   完了日
 *   }
 * - onRemove() => task 削除関数
 * - onUpdate(task) => task 更新関数
 */
export default {
  props: ['task', 'onRemove', 'onUpdate'],
  methods: {
    // 編集ダイアログ表示
    onEdit() {
      this.$buefy.modal.open({
        parent: this,
        props: {
          task: this.task,
          onUpdate: this.onUpdate,
        },
        component: EditDialog,
        hasModalCard: true,
        fullScreen: true,
        trapFocus: true
      })
    },
    // 詳細ダイアログ表示
    onShow() {
      this.$buefy.modal.open({
        parent: this,
        props: {
          task: this.task,
        },
        component: DetailDialog,
        hasModalCard: true,
        fullScreen: true,
        trapFocus: true
      })
    },

    // 日付データを表示
    displayDatetime(date) {
      return date? moment(date).format('YYYY/MM/DD HH:mm'): ''
    },

    // タスクカードの class を取得: 状態による色変更
    getTaskClass() {
      if (this.task.end_date) {
        // 完了タスク
        return 'is-completed'
      }
      // 現在日時と締切日時の差分から文字色変更
      if (!this.task.limit_date) {
        return ''
      }
      const diff = moment(this.task.limit_date).diff(moment(), 'minutes')
      if (diff < 0) {
        // 締切日超過
        return 'is-out'
      }
      if (diff <= 60 * 24) {
        // 本日締切
        return 'is-limit'
      }
      return ''
    }
  },
}
</script>

<style scoped lang="scss">
/* Scoped SCSS */

.card:hover {
  /* タスクカードを浮かせる */
  box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.25);
  transform: translateY(-0.1875em);
}

.is-completed {
  /* 完了タスク */
  color: #444;
  background-color: #aaa;
  .card-header-title {
    color: #444;
    font-weight: bold;
    &.button {
      color: white;
    }
  }
}

.is-limit {
  /* 本日締め切り */
  color: #0b6;
  background-color: #ffd;
  .card-header-title {
    color: #0b6;
    font-weight: bold;
    &.button {
      color: white;
    }
  }
}

.is-out {
  /* 期限切れ */
  color: #e40;
  background-color: #fdf;
  .card-header-title {
    color: #e40;
    font-weight: bold;
    &.button {
      color: white;
    }
  }
}
</style>