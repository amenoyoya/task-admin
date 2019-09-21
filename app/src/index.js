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

// parts
import DetailDialog from './components/parts/DetailDialog';
import EditDialog from './components/parts/EditDialog';

// components
import Home from './components/Home';

Vue.component('detail-dialog', DetailDialog);
Vue.component('edit-dialog', EditDialog);

new Vue({
  render: h => h(Home)
}).$mount('#app');
