import Vue from 'vue';
import VueRouter from 'vue-router';
import App from './App.vue';

Vue.use(VueRouter);

// This router is only defined to read the query params of a previous session
const router = new VueRouter({
  mode: 'hash',
  routes: [
    { path: '/:photoid', name: 'photo', component: App },
  ],
});

// eslint-disable-next-line no-new
new Vue({
  router,
  el: '#app',
  render: h => h(App),
});
