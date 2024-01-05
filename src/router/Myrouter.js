// src/router/Myrouter.js
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/components/MyMenu.vue'), // 請確保你已經創建了 Home.vue 這個組件*/
  },
  {
    path: '/new-page',
    name: 'NewPage',
    component: () => import('@/view/Learning_notes.vue'), // 創建一個新的組件 NewPage.vue*/
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;