// src/.main.js
import { createApp } from 'vue'
import App from './App.vue'
import myrouter from './router/index.js';
import './assets/styles/global.css';

const app = createApp(App)
app.use(myrouter);
app.mount('#app')