<template>
  <div>
    <nav>
      <router-link to="/">Главная</router-link> |
      <router-link to="/login">Вход</router-link> |
      <router-link to="/register">Регистрация</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style>
nav {
  padding: 10px;
  background: #eee;
}
nav a {
  margin-right: 10px;
}
</style>
