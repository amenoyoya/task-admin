<template>
<div class="modal-card">
  <header class="modal-card-head">
    <p class="modal-card-title" v-html="detail_task.title"></p>
  </header>
  <section class="modal-card-body">
    <b-field grouped>
      <div class="control">
        <b-taglist attached>
            <b-tag type="is-dark"><i class="fas fa-hourglass-start"></i></b-tag>
            <b-tag type="is-info">{{detail_task.start_date}}</b-tag>
        </b-taglist>
      </div>
      <div class="control">
        <b-taglist attached>
          <b-tag type="is-dark"><i class="fas fa-hourglass-end"></i></b-tag>
          <b-tag type="is-info">{{detail_task.limit_date}}</b-tag>
        </b-taglist>
      </div>
      <div class="control">
        <b-taglist attached>
          <b-tag type="is-dark"><i class="fas fa-check"></i></b-tag>
          <b-tag type="is-info">{{detail_task.end_date}}</b-tag>
        </b-taglist>
      </div>
    </b-field>
    <div class="content" v-html="content"></div>
  </section>
  <footer class="modal-card-footer">
    <button class="button" type="button" @click="$parent.close()">Close</button>
  </footer>
</div>
</template>

<script>
import marked from 'marked';

export default {
  props: ['detail_task'],
  data() {
    return {
      content: ''
    };
  },
  async mounted() {
    this.content = marked(this.detail_task.content);
  }
}
</script>
