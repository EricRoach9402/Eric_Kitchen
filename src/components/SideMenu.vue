<template>
    <div>
      <!-- 選單按鈕 -->
      <button @click="toggleMenu">Toggle Menu</button>
  
      <!-- 選單區塊 -->
      <div :class="{ 'menu-open': isMenuOpen }">
        <!-- 選單內容 -->
        <div>
          <!-- 其他選單內容 -->
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isMenuOpen: true,
      };
    },
    methods: {
      toggleMenu() {
        this.isMenuOpen = !this.isMenuOpen;
      },
    },
  };
  </script>
  
  <style>
  .menu-open {
    width: 200px;
    /* 其他樣式設置 */
  }
  </style>
  