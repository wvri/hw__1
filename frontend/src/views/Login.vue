<template>
    <div class="container">
      <h2>Вход</h2>
      <form @submit.prevent="login">
        <div>
          <label>Email:</label>
          <input type="email" v-model="email" required />
        </div>
        <div>
          <label>Пароль:</label>
          <input type="password" v-model="password" required />
        </div>
        <button type="submit">Войти</button>
      </form>
      <p>Нет аккаунта? <router-link to="/register">Зарегистрироваться</router-link></p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        email: '',
        password: ''
      };
    },
    methods: {
      async login() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/token/', {
            email: this.email,
            password: this.password
          });
          console.log('Токен:', response.data);
          alert('Вход успешен!');
        } catch (error) {
          console.error('Ошибка входа', error);
          alert('Неправильный email или пароль');
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  </style>
  