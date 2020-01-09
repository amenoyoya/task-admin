<template>
<form class="form">
  <div class="modal-card">
    <header class="modal-card-head">
      <p class="modal-card-title">タスク編集</p>
    </header>
    <section class="modal-card-body">
      <b-field label="Title">
        <b-input v-model="title"></b-input>
      </b-field>
      <b-field label="開始日">
        <ctk-datetime-picker v-model="start_date" format="YYYY-MM-DD HH:mm" />
      </b-field>
      <b-field label="締切日">
        <ctk-datetime-picker v-model="limit_date" format="YYYY-MM-DD HH:mm" />
      </b-field>
      <b-field label="Content">
        <b-input type="textarea" v-model="content"></b-input>
      </b-field>
    </section>
    <footer class="modal-card-footer">
      <button class="button" type="button" @click="$parent.close()">Close</button>
      <button class="button is-primary" @click.prevent="saveTask">完了</button>
    </footer>
  </div>
</form>
</template>

<script>
export default {
  props: ['edit_task'],
  data() {
    return {
      title: '',
      content: '',
      start_date: '',
      limit_date: '',
    };
  },
  
  methods: {
    saveTask() {
      this.edit_task.title = this.title;
      this.edit_task.content = this.content;
      this.edit_task.start_date = this.start_date;
      this.edit_task.limit_date = this.limit_date;
      this.$emit('putTasks'); // タスク更新API実行
      this.$parent.close();
    }
  },

  mounted() {
    this.title = this.edit_task.title;
    this.content = this.edit_task.content;
    this.start_date = this.edit_task.start_date;
    this.limit_date = this.edit_task.limit_date;
  }
}
</script>
