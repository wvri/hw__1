import { createApp } from 'vue';
import App from './App.vue';
import router from './router';  // Подключаем маршрутизатор

const app = createApp(App);
app.use(router); // Используем маршрутизацию
app.mount('#app');
