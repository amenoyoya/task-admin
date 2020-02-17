<template>
  <section class="section">
    <div class="container">
      <h1 class="title">
        タスク管理アプリ&nbsp;
        <a class="button is-danger" @click.prevent="addTask"><i class="fas fa-plus-square"></i>&nbsp;タスク追加</a>
      </h1>
      <!--
        - タスクパネルをMasonryで整列
        - 整列時のトランジション時間を 0.2 秒とする
      -->
      <div v-masonry transition-duration="0.2s">
        <!--
          - 各タスクパネルをMasonryタイル（整列対象）とする
          - 各タイルのスタイルを Scoded CSS で定義: .masonry-tile
        -->
        <div v-masonry-tile class="masonry-tile">
          <!-- Use Panel component as task-panel -->
          <task-panel title="未着手" aria_id="panel_1" class_name="is-warning" :task_lists="task_lists" :task_list_index="0" />
        </div>
        <div v-masonry-tile class="masonry-tile">
          <task-panel title="実行中" aria_id="panel_2" class_name="is-success" :task_lists="task_lists" :task_list_index="1" />
        </div>
        <div v-masonry-tile class="masonry-tile">
          <task-panel title="保留・確認中" aria_id="panel_1" class_name="is-info" :task_lists="task_lists" :task_list_index="2" />
        </div>
        <div v-masonry-tile class="masonry-tile">
          <task-panel title="完了" aria_id="panel_1" class_name="is-primary" :task_lists="task_lists" :task_list_index="3" />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  methods: {
    // 新規タスク追加
    addTask() {
      // 未着手タスクリストに新規追加（見やすさのため、リストの頭に追加する）
      this.task_lists[0].unshift({title: '', start_date: '', limit_date: ''})
      // DOM更新後にMasonryによる整列を実行
      this.$nextTick(function() {
        this.$redrawVueMasonry()
      })
    },
  },

  // 起動時にタスクリスト読み込む
  mounted() {
    this.loadTasksAndRedrawMasonry()
  },
}
</script>

<style scoped>
/* Scoped CSS */
.masonry-tile {
  width: 300px;
  margin: 10px;
}
</style>