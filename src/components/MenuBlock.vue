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
          <!-- 遍歷菜單項目，顯示 checkbox 和標籤 -->
          <li v-for="(item, index) in items" :key="index">
            <input 
              type="checkbox" 
              :id="`item-${title}-${index}`" 
              v-model="item.selected"
              @change="handleCheckboxChange(item)"
            />
            <label :for="`item-${title}-${index}`" @click.stop>{{ item.name }}</label>
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
  // 當 checkbox 狀態改變時觸發的方法
  methods: {
    handleCheckboxChange(item) {
      // 當 checkbox 狀態改變時，更新 selectedItems
      if (item.selected) {
        this.$emit('item-selected', item); // 觸發父組件事件，將選中的項目傳遞給父組件
      } else {
        this.$emit('item-deselected', item); // 觸發父組件事件，將取消選中的項目傳遞給父組件
      }
    },
  },
});
</script>

<style scoped>
/*將 menu-head 設為水平排列*/
.menu-head {
  display: flex;
  margin-bottom: 15px; /*head與下方菜色的距離*/
}

/* 調整圖標和標題之間的間距 */
.menu-icon {
  margin-top: 15px;
  margin-right: 50px; 
}
/* 設定title */
.menu-title {
  font-size: 26px;
}
/*設定菜單列表容器 */
.menu-list {
  list-style: none; /*移除列表前方的「·」 */
  grid-template-columns: 1fr;
}
/*設定菜單內品項間的距離及字體大小 */
.menu-list li {
  display: flex;
  margin-bottom: 22px;
  font-size: 26px;
  padding:6%;
}
/*設定各列間的距離 */
.listnone {
  margin-bottom: 15px;
}
/*設定checkbox被選取後的顏色 */
input[type="checkbox"]:checked + label {
  color: #e40c0c;
}
</style>