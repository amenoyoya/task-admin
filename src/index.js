// Vue
import Vue from 'vue';
import 'babel-polyfill'; // IE11 polyfill

// Buefy
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
Vue.use(Buefy);

// CtkDatetimePicker
import VueCtkDateTimePicker from 'vue-ctk-date-time-picker';
import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.css';
Vue.component('ctk-datetime-picker', VueCtkDateTimePicker);

// masonry
import {VueMasonryPlugin} from 'vue-masonry';
Vue.use(VueMasonryPlugin);

// VueDraggable
import VueDraggable from 'vuedraggable';
Vue.component('draggable', VueDraggable);

// parts
import DetailDialog from './components/parts/DetailDialog';
import EditDialog from './components/parts/EditDialog';
Vue.component('detail-dialog', DetailDialog);
Vue.component('edit-dialog', EditDialog);

// components
import Home from './components/Home';

new Vue({
  render: h => h(Home)
}).$mount('#app');
