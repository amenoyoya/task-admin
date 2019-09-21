import Vue from 'vue';
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
import 'babel-polyfill'; // IE11 polyfill

// parts
import EditDialog from './components/parts/EditDialog';

// components
import Home from './components/Home';

Vue.use(Buefy);
Vue.component('edit-dialog', EditDialog);

new Vue({
  render: h => h(Home)
}).$mount('#app');
