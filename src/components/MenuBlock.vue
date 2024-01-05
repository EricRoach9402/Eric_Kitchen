<!-- src/components/MenuBlock.vue -->
<template>
  <div>
    <div class="menu-block mb60">
      <div class="menu-head">
        <span class="menu-icon">
          <TitleIconComponent :iconImageSrc="iconImageSrc" :iconSize="iconSize" />
        </span>
        <h2 class="menu-title">{{ title }}</h2>
      </div>
      <div class="menu-list">
        <ul class="listnone">
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
    iconSize: Object, // 修改這一行
  },
  
  setup(props) {
    const iconImageSrc = `/images/icon/${props.icon}.png`;

    return {
      iconImageSrc,
    };
  },
  components: {
    TitleIconComponent,
  },
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
.menu-head {
  margin-bottom: 10px;
  display: flex;
}

.menu-icon {
  margin-top: 15px;
  margin-right: 50px; /* 调整图标和标题之间的间距 */
}
.menu-head {
  margin-bottom: 15px;
}

.menu-title {
  font-size: 26px;
}

.menu-block {
  text-align: center;
}

.menu-list {
  list-style: none;
  padding: 0;
  display: grid;
  grid-template-columns: 1fr;
  justify-content: center;
  align-items: center;
}

.menu-list li {
  display: flex;
  align-items: center;
  text-align: center;
  margin-bottom: 5px;
  font-size: 20px;
}

.menu-list li input {
  margin-left: 50px;
  margin-right: 30px;
}

.listnone {
  list-style-type: none;
  padding: 0;
  margin: 0;
  margin-bottom: 15px;
}

input[type="checkbox"]:checked + label {
  color: #e40c0c;
}
</style>