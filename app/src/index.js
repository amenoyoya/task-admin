import Vue from 'vue';
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';
import 'babel-polyfill'; // IE11 polyfill

// components
import Home from './components/Home';

Vue.use(Buefy);

new Vue({
  render: h => h(Home)
}).$mount('#app');
