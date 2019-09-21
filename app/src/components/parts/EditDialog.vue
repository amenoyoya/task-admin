<template>
<form class="form">
  <div class="modal-card" style="width: auto">
    <header class="modal-card-head">
      <p class="modal-card-title">タスク編集</p>
    </header>
    <section class="modal-card-body">
      <b-field label="Title">
        <b-input v-model="edit_task.title"></b-input>
      </b-field>
      <b-field label="開始日">
        <b-datepicker
            placeholder="Type or select a date..."
            icon="calendar-today"
            editable>
        </b-datepicker>
      </b-field>
      <b-field label="締切日">
          <b-datepicker
              placeholder="Type or select a date..."
              icon="calendar-today"
              editable>
          </b-datepicker>
      </b-field>
      <b-field label="Content">
        <b-input type="textarea" v-model="edit_task.content"></b-input>
      </b-field>
    </section>
    <footer class="modal-card-footer">
      <button class="button" type="button" @click="$parent.close()">Close</button>
      <button class="button is-primary">完了</button>
    </footer>
  </div>
</form>
</template>

<script>
export default {
  props: ['edit_task'],
}
</script>
