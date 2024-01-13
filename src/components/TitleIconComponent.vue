<!-- src/components/TitleIconComponent.vue -->
<template>
    <div class="title-icon-container">
      <img :src="iconImageSrc" :width="iconSize.width" :height="iconSize.height" alt="Icon" />
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  
  export default defineComponent({
    props: {
      iconImageSrc: String,
      iconSize: Object,
    },
  });
  </script>
  
  <style scoped>
  img {
    display: block;
    margin: 0 auto;
  }
  </style>