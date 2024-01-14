// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import MyMenu from '../view/MyMenu.vue';
import ManagerView from '../view/ManagerView.vue';

const routes = [
  {
    path: '/',
    name: 'MyMenuName',
    component: MyMenu,
  },
  {
    path: '/manager',
    name: 'ManagerViewName',
    component: ManagerView,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;