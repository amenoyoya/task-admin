<template>
  <div class="modal-card" style="width: auto; height: 100%">
    <header class="modal-card-head">
      <p class="modal-card-title">{{ task.title }}</p>
    </header>
    <section class="modal-card-body">
      <b-field grouped>
        <!-- 開始日 -->
        <div class="control">
          <b-taglist attached>
              <b-tag type="is-dark"><b-icon pack="fas" icon="hourglass-start" /></b-tag>
              <b-tag type="is-info">{{ task.start_date }}</b-tag>
          </b-taglist>
        </div>
        <!-- 締切日 -->
        <div class="control">
          <b-taglist attached>
            <b-tag type="is-dark"><b-icon pack="fas" icon="hourglass-end" /></b-tag>
            <b-tag type="is-info">{{ task.limit_date }}</b-tag>
          </b-taglist>
        </div>
      </b-field>
      <!-- タスク詳細 -->
      <div class="content" v-html="task.content"></div>
    </section>
    <footer class="modal-card-footer">
      <b-button @click.prevent="$parent.close()">Close</b-button>
    </footer>
  </div>
</template>

<script>
/**
 * props として以下の値を親コンポーネントから受け取る
 * - task {
 *     title <string>:      タスク名
 *     content <string>:    内容
 *     start_date <string>: 開始日
 *     limit_date <string>: 締切日
 *   }
 */
export default {
  props: ['task'],
}
</script>

<style>
/** 
 * QuillEditorのインデントスタイルを適用
 * => 外部Vueコンポーネント内部の要素に対するスタイル適用のため Scoped CSS は使えない
 */
.content .ql-indent-1 {
  margin-left: 1em;
}
.content .ql-indent-2 {
  margin-left: 2em;
}
.content .ql-indent-3 {
  margin-left: 3em;
}
.content .ql-indent-4 {
  margin-left: 4em;
}
.content .ql-indent-5 {
  margin-left: 5em;
}
</style>