import Vue from 'vue';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import App from './App.vue';
import router from './router';
import store from './store';

Vue.config.productionTip = false;
Vue.use(BootstrapVue);

new Vue({
  router,
  store,
  created() {
    // what to do when the element is created
    console.log('loaded...');

    // load all links when the page is loaded first time
    this.$store.dispatch('fetchAllLinks');
  },
  render: h => h(App),
}).$mount('#app');
