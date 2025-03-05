<template>
    <div class="container">
      <h2>Регистрация</h2>
      <form @submit.prevent="register">
        <div>
          <label>Email:</label>
          <input type="email" v-model="email" required />
        </div>
        <div>
          <label>Пароль:</label>
          <input type="password" v-model="password" required />
        </div>
        <div>
          <label>Повторите пароль:</label>
          <input type="password" v-model="confirmPassword" required />
        </div>
        <button type="submit">Зарегистрироваться</button>
      </form>
      <p>Уже есть аккаунт? <router-link to="/login">Войти</router-link></p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        email: '',
        password: '',
        confirmPassword: ''
      };
    },
    methods: {
      async register() {
        if (this.password !== this.confirmPassword) {
          alert('Пароли не совпадают!');
          return;
        }
  
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/register/', {
            email: this.email,
            password: this.password
          });
          console.log('Успешная регистрация:', response.data);
          alert('Регистрация успешна! Теперь войдите в аккаунт.');
          this.$router.push('/login');
        } catch (error) {
          console.error('Ошибка регистрации', error);
          alert('Ошибка при регистрации');
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
  