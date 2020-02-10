<template>
  <b-form>
    <div class="modal-card" style="width: auto; height: 100%">
      <header class="modal-card-head">
        <p class="modal-card-title">タスク編集</p>
      </header>
      <section class="modal-card-body">
        <b-field label="Title">
          <b-input v-model="title" />
        </b-field>
        <b-field label="開始日">
          <!-- 年月日 時分 を 24時間形式で選択するDatetimePicker -->
          <ctk-datetime-picker v-model="start_date" format="YYYY-MM-DD HH:mm" />
        </b-field>
        <b-field label="締切日">
          <ctk-datetime-picker v-model="limit_date" format="YYYY-MM-DD HH:mm" />
        </b-field>
        <b-field label="Content">
          <quill-editor class="quill-wrap" v-model="content" />
        </b-field>
      </section>
      <footer class="modal-card-footer">
        <b-button @click.prevent="$parent.close()">Close</b-button>
        <b-button class="is-primary" @click.prevent="saveTask">完了</b-button>
      </footer>
    </div>
  </b-form>
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
 * - onUpdate(task) => task 更新関数
 */
export default {
  props: ['task', 'onUpdate'],
  data() {
    return {
      title: '',
      content: '',
      start_date: '',
      limit_date: '',
    }
  },
  
  methods: {
    // 親コンポーネントから渡されたタスクに編集結果を反映
    saveTask() {
      this.onUpdate({
        title: this.title,
        content: this.content,
        start_date: this.start_date,
        limit_date: this.limit_date,
      })
      this.$parent.close()
    }
  },

  // マウント時、親コンポーネントから渡されたタスクの内容をコピー
  mounted() {
    this.title = this.task.title
    this.content = this.task.content
    this.start_date = this.task.start_date
    this.limit_date = this.task.limit_date
  }
}
</script>

<style>
/**
 * QuillEditor のツールバーを固定する
 * => 外部Vueコンポーネント内部の要素に対するスタイル適用のため Scoped CSS は使えない
 */
.ql-container {
  /* Quillエディタ部の最大高さを ViewPort の30％に固定してオーバーフローをスクロールさせる */
  max-height: 30vh;
  overflow: auto;
}
</style>