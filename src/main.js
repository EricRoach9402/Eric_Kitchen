// src/.main.js
import { createApp } from 'vue'
import App from './App.vue'
import MyMenu from './components/MyMenu.vue'
import MyHeader from './components/MyHeader.vue';
import './assets/styles/global.css';
import myrouter from './router/Myrouter.js';

const app = createApp(App)
app.component('My-Menu', MyMenu) 
app.component('My-Header', MyHeader) 
app.component('MyRouter', myrouter) 
app.mount('#app')