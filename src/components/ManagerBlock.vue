<!-- src/components/MenuBlock.vue -->
<template>
    <div>
      <div class="menu-block">
        <div class="menu-head">
          <span class="menu-icon">
            <!-- 使用 TitleIconComponent 組件顯示圖標 -->
            <TitleIconComponent :iconImageSrc="iconImageSrc" :iconSize="iconSize" />
          </span>
          <!-- 菜單標題 -->
          <h2 class="menu-title">{{ title }}</h2>
        </div>
        <!-- 菜單列表 -->
        <div class="menu-list">
          <ul class="listnone">
            <!-- 遍歷菜單項目，顯示標籤和輸入框 -->
            <li v-for="(item, index) in items" :key="index" class="menu-item">
              <label class="item-label">{{ item.name }}</label>
              <input v-model="item.quantity" class="item-input" placeholder="請輸入數量" />
              <span class="item-unit">份</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import TitleIconComponent from './TitleIconComponent.vue';
  
  export default defineComponent({
    props: {
      title: String,
      items: Array,
      icon: String,
      iconSize: Object, 
    },
    // 設定圖標的路徑
    setup(props) {
      const iconImageSrc = `/images/icon/${props.icon}.png`;
  
      return {
        iconImageSrc,
      };
    },
    components: {
      TitleIconComponent,
    },
  });
  </script>
  
  <style scoped>
  /* 添加樣式以美化標籤和輸入框 */
  .menu-block {
    margin-bottom: 20px; /* 調整整體區塊的底部間距 */
  }
  
  .menu-head {
    display: flex;
    margin-bottom: 15px; /* head 與下方菜色的距離 */
  }
  
  .menu-icon {
    margin-top: 15px;
    margin-right: 50px; 
  }
  
  .menu-title {
    font-size: 26px;
  }
  
  .menu-list {
    list-style: none;
    grid-template-columns: 1fr;
  }
  
  .menu-list li {
    display: grid; /* 使用 grid 進行排列 */
    grid-template-columns: 1fr 80px 1fr; /* 將每一項劃分為三列，標籤、輸入框和單位 */
    align-items: center;
    margin-bottom: 5px;
    font-size: 20px;
  }
  
  .item-label {
    text-align: left; /* 將標籤右對齊 */
    padding-right: 10px; /* 加入右邊距 */
  }
  
  .item-input {
    width: 60px; /* 調整輸入框寬度 */
    padding: 10px 15px;
  }
  
  .item-unit {
    font-size: 18px;
    padding:22%;
  }
  </style>
  