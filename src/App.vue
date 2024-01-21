<!-- src/App.vue -->
<template>
  <div>
    <router-view />
    <SideMenu />
  </div>
</template>
<script>
import SideMenu from './components//SideMenu.vue';

export default {
  components: {
    SideMenu,
  },
  // 其他設定和方法
};
</script>
