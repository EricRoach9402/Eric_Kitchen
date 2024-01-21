<!-- Menu.vue -->

<template>
  <div>
    <div class="page-header">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
            <div class="page-caption">
              <h2 class="page-title">艾瑞克廚房</h2>
              <p>M E N U</p>
            </div>
            <div class="switch-button">
              <button class="manager-button-style" @click="ManagerButton">切換管理員系統</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="space-medium">
      <!-- MenuBlock.vue 的容器 -->
      <div class="container">
        <!-- 水平排列的 MenuBlock.vue -->
        <div class="row_1">
          <div class="column1_1">
            <MenuBlock 
              title="開胃菜" 
              icon="icon-hamburger" 
              :items="starters" 
              :iconSize="{ width: 70, height: 60 }"       
              @item-selected="handleItemSelected"
              @item-deselected="handleItemDeselected"
              />
          </div>
          <div class="column1_2">
            <MenuBlock 
            title="蔬菜" 
            icon="icon-salad" 
            :items="salads" 
            :iconSize="{ width: 50, height: 50 }"
            @item-selected="handleItemSelected"
            @item-deselected="handleItemDeselected"
            />
          </div>
          <div class="column1_3">
            <MenuBlock 
            title="主食" 
            icon="icon-bibimbap" 
            :items="special_dishes" 
            :iconSize="{ width: 50, height: 50 }"
            @item-selected="handleItemSelected"
            @item-deselected="handleItemDeselected"
            />
          </div>
        </div>
        <div class="row_2">
          <div class="column2_1">
            <MenuBlock 
              title="飲料" 
              icon="icon-drink" 
              :items="drinks" 
              :iconSize="{ width: 50, height: 50 }"
              @item-selected="handleItemSelected"
              @item-deselected="handleItemDeselected"
            />
          </div>
          <div class="column2_2">
            <MenuBlock 
              title="甜點" 
              icon="icon-primary" 
              :items="dessert" 
              :iconSize="{ width: 50, height: 50 }"
              @item-selected="handleItemSelected"
              @item-deselected="handleItemDeselected"
            />
          </div>
          <div class="column2_3">
            <MenuBlock 
              title="冰品" 
              icon="icon-icecream" 
              :items="ice_cream" 
              :iconSize="{ width: 50, height: 50 }"
              @item-selected="handleItemSelected"
              @item-deselected="handleItemDeselected"
            />
          </div>
        </div>
        <div class="submit-button">
          <button class="button-style" @click="submitMenu">送出</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import MenuBlock from '../components/MenuBlock.vue';
export default {
  components: {
    MenuBlock,
  },
  data() {
    return {
      starters: [      
        { name: '鹹派', selected: false},
        { name: '蝦仁派', selected: false},
        { name: '炸雞翅', selected: false},
        { name: '炸薯條', selected: false},
        { name: '炸雞塊', selected: false},
        { name: '烤蔬菜串', selected: false},
        { name: '鹽烤甜椒', selected: false},
      ],
      salads: [
        { name: '凱薩沙拉', selected: false},
        { name: '蒜香炒青菜', selected: false},
        { name: '青椒炒肉絲', selected: false},
        { name: '炒花椰菜', selected: false},
        { name: '高麗菜炒豆皮', selected: false},
      ],
      special_dishes:[
        { name: '火鍋', selected: false},
        { name: '沙茶肉片', selected: false},
        { name: '蒜香肉片', selected: false},
        { name: '糖醋魚', selected: false},
        { name: '香煎魚', selected: false},
        { name: '鹽烤魚', selected: false},
        { name: '漢堡肉', selected: false},
      ],
      drinks:[
        { name: '咖啡', selected: false},
        { name: '紅茶', selected: false},
        { name: '綠茶', selected: false},
        { name: '奶茶', selected: false},
        { name: '可樂', selected: false},
        { name: '汽水', selected: false},
        { name: '水果茶', selected: false},
      ],
      dessert:[
        { name: '布丁', selected: false},
        { name: '蘋果派', selected: false},
        { name: '曲奇餅', selected: false},
        { name: '馬卡龍', selected: false},
        { name: '蛋糕捲', selected: false},
        { name: '杯子蛋糕', selected: false},
        { name: '奶酪蛋糕', selected: false},
      ],
      ice_cream:[
        {name:'巧克力雪糕', selected: false},
        {name:'小美冰淇淋', selected: false},
        {name:'冰淇淋泡芙', selected: false},
      ],
      selectedItems: [], // 存儲已勾選的項目
    };
  },
  methods: {
    handleItemSelected(item) {
      this.selectedItems.push(item);
    },
    handleItemDeselected(item) {
      this.selectedItems = this.selectedItems.filter((i) => i !== item);
    },
    ManagerButton(){
      this.$router.push('/manager');
    },
    submitMenu() {
      // 處理送出邏輯，可以使用 this.selectedItems
      console.log('已勾選的項目：', this.selectedItems);
      // 在這裡可以將 this.selectedItems 送出到後端或進行其他處理
      // 使用 window.alert 顯示已選擇的菜品名稱
      const selectedItemsNames = this.selectedItems.map((item) => item.name).join(', ');
      window.alert(`選擇的菜色為：${selectedItemsNames}`);
      //包裝Json檔
        const jsonData = JSON.stringify({
          name: selectedItemsNames,
          table_name:"MenuItem"
      });

      // 發送 POST 请求
  fetch('http://127.0.0.1:5000/api', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: jsonData,
  })
    .then(response => response.json())
    .then(data => {
      // 處理 API 返回的數據
      console.log('API 返回的數據:', data);

      // 彈出成功提示框
      window.alert('菜單信息已成功提交！');
    })
    .catch(error => {
      // 處理错误
      console.error('POST 請求失敗:', error);

      // 彈出错誤提示框
      window.alert('發送菜單信息失敗，請稍后重試。');
    });
    },
  },
};
</script>

<style scoped>
/*控制標題 */
.page-caption {
  text-align: center; /* 將文本水平置中 */
  margin: 0 auto; /* 通過 margin 屬性實現水平居中，0表示上下不留白，auto表示左右自動分配空間 */
  font-size: 24px;
}
.container{
  display: grid;
}
.row_1{
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 0px; /* 設置間隔 */
  border-top: 3px solid #000; /* 只畫上邊 */
  border-bottom: 1px dashed  #777474; /* 只畫下邊 */
}
.row_2 {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 0px; /* 設置間隔 */
  border-top: 1px dashed  #777474; /* 只畫上邊 */
  border-bottom: 3px solid #000; /* 只畫下邊 */
  
}
.row_1 .column1_1 {
  grid-column-start: 2;
  grid-column-end: 3;
  }

.row_1 .column1_2 {
  grid-column-start: 3;
  grid-column-end: 4;
}

.row_1 .column1_3 {
  grid-column-start: 4;
  grid-column-end: 5;
}

.row_2 .column2_1 {
  grid-column-start: 2;
  grid-column-end: 3;
}

.row_2 .column2_2 {
  grid-column-start: 3;
  grid-column-end: 4;
}

.row_2 .column2_3 {
  grid-column-start: 4;
  grid-column-end: 5;
}
.switch-button{
  margin: 1% 1%; /* 上右下左的順序，1% 表示上下留白 1%，左右留白 1% */
  position: absolute;
  top: 0;
  right: 0;
}
.manager-button-style{
  background-color: #9e8e96; /* Green背景 */
  border: none; /* 移除邊框 */
  color: white; /* 文字顏色為白色 */
  padding: 15px 25px; /* 內間距 */
  text-align: center; /* 文字居中 */
  text-decoration: none; /* 移除超連結效果 */
  display: inline-block; /* 設定元素為內聯塊級元素，使得寬高生效 */
  font-size: 18px; /* 字體大小 */
  margin: 3px 20px; /* 外邊距 */
  cursor: pointer; /* 鼠標樣式為手型 */
  border-radius: 8px; /* 圓角 */
}
.submit-button{
  margin: 0.8% auto; /* 通過 margin 屬性實現水平居中，0表示上下不留白，auto表示左右自動分配空間 */
}
.button-style{
  background-color: #088828; /* Green背景 */
  border: none; /* 移除邊框 */
  color: white; /* 文字顏色為白色 */
  padding: 8px 25px; /* 內間距 */
  text-align: center; /* 文字居中 */
  text-decoration: none; /* 移除超連結效果 */
  display: inline-block; /* 設定元素為內聯塊級元素，使得寬高生效 */
  font-size: 16px; /* 字體大小 */
  margin: 3px 2px; /* 外邊距 */
  cursor: pointer; /* 鼠標樣式為手型 */
  border-radius: 8px; /* 圓角 */
  }
</style>