// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import MyMenu from '../view/MyMenu.vue';
import ManagerView from '../view/ManagerView.vue';
import MyOrder from '../view/MyOrder.vue';

const routes = [
  {
    path: '/',
    name: 'MyMenuName',
    component: MyMenu,
  },
  {
    path: '/manager',
    name: 'ManagerView',
    component: ManagerView,
  },
  {
    path: '/myorder',
    name: 'MyOrder',
    component: MyOrder,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;