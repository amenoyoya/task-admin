<template>
  <b-collapse class="panel" :open.sync="isOpen" :aria-id="aria_id">
    <div slot="trigger" :class="'panel-heading notification ' + class_name" role="button" :aria-controls="aria_id">
      <strong>{{ title }}</strong>
    </div>
    <div class="panel-block">
      <!-- VueDraggable -->
      <!--
        - タスク列間でドラッグ＆ドロップできるように group を指定: 同じグループ名の draggable 間でデータのやり取りが可能
        - ドラッグ前と後におけるタスク列のindex情報を data-group に保持
        - タスク列が空になってもドロップできるよう、タイル要素にする（class: tile is-parent is-vertical）
      -->
      <draggable
        group="task_admin" :data-group="task_list_index" v-model="task_lists[task_list_index]"
        class="tile is-parent is-vertical" @end="onDrop"
      >
        <!-- 各タスクカードは子タイル要素にする（class: tile is-child） -->
        <div v-for="(task, i) in task_lists[task_list_index]" :key="aria_id + '_' + i" class="tile is-child">
          <!-- Use Card component as task-card
            - ドラッグ可能なことが分かりやすいように cursor: move に
            - onRemove prop に removeTask(i) を実行する関数を渡す
            - onUpdate prop に updateTask(i, task) を実行する関数を渡す
          -->
          <task-card
            :task="task" style="cursor: move" :onRemove="() => removeTask(i)" :onUpdate="(task) => updateTask(i, task)"
          />
        </div>
      </draggable>
    </div>
  </b-collapse>
</template>

<script>
import moment from 'moment'

/**
 * props として以下の値を親コンポーネントから受け取る
 * - title <string>:      パネル名
 * - aria_id <string>:    パネル識別ID
 * - class_name <string>: "is-primary"|"is-success"|"is-info"|"is-warning"|"is-danger"|...
 * - task_lists <array[array[task]]>:  @see Card.vue
 * - task_list_index <int>:            タスク列の index
 */
export default {
  props: ['title', 'aria_id', 'class_name', 'task_lists', 'task_list_index'],
  methods: {
    // タスク削除
    removeTask(index) {
      this.task_lists[this.task_list_index].splice(index, 1)
      // タスクリスト保存 & Masonry再整列
      this.saveTasksAndRedrawMasonry()
    },

    // タスク更新
    updateTask(index, newTask) {
      this.$set(this.task_lists[this.task_list_index], index, newTask)
      // タスクリスト保存 & Masonry再整列
      this.saveTasksAndRedrawMasonry()
    },

    // タスクカードDrop時イベント
    onDrop(evt) {
      // 完了タスク以外から完了タスクに移動したら、完了日（＝現在日時）セット
      const completed_index = 3
      if (evt.from.dataset.group != completed_index && evt.to.dataset.group == completed_index) {
        this.$set(this.task_lists[completed_index][evt.newIndex], 'end_date', moment().format('YYYY-MM-DD HH:mm'))
      }
      // 完了タスクから完了タスク以外に移動したら、完了日を削除
      if (evt.from.dataset.group == completed_index && evt.to.dataset.group != completed_index) {
        this.$set(this.task_lists[evt.to.dataset.group][evt.newIndex], 'end_date', null)
      }
      // ドロップ時にMasonry再整列 & タスクリスト保存 実行
      this.saveTasksAndRedrawMasonry()
    }
  },
}
</script>
