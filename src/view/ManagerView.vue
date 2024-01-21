<!-- src/views/ManagerView.vue -->

<template>
  <div>
    <div class="page-header">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
            <div class="page-caption">
              <h2 class="page-title">管理員系統</h2>
              <p>庫 存 管 理</p>
            </div>
            <div class="switch-button">
              <button class="menu-button-style" @click="MenuButton">切換 MENU</button>
            </div>
            <div class="myorder-button">
              <button class="myorder-button-style" @click="MyOrderButton">切換 訂單管理系統</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="space-medium">
      <!-- ManagerBlock.vue 的容器 -->
      <div class="container">
        <!-- 水平排列的 ManagerBlock.vue -->
        <div class="row_1">
          <div class="column1_1">
            <ManagerBlock 
              title="開胃菜" 
              icon="icon-hamburger" 
              :items="starters" 
              :iconSize="{ width: 70, height: 60 }"       
              />
          </div>
          <div class="column1_2">
            <ManagerBlock 
            title="蔬菜" 
            icon="icon-salad" 
            :items="salads" 
            :iconSize="{ width: 50, height: 50 }"
            />
          </div>
          <div class="column1_3">
            <ManagerBlock 
            title="主食" 
            icon="icon-bibimbap" 
            :items="special_dishes" 
            :iconSize="{ width: 50, height: 50 }"
            />
          </div>
        </div>
        <div class="row_2">
          <div class="column2_1">
            <ManagerBlock 
              title="飲料" 
              icon="icon-drink" 
              :items="drinks" 
              :iconSize="{ width: 50, height: 50 }"
            />
          </div>
          <div class="column2_2">
            <ManagerBlock 
              title="甜點" 
              icon="icon-primary" 
              :items="dessert" 
              :iconSize="{ width: 50, height: 50 }"
            />
          </div>
          <div class="column2_3">
            <ManagerBlock 
              title="冰品" 
              icon="icon-icecream" 
              :items="ice_cream" 
              :iconSize="{ width: 50, height: 50 }"
            />
          </div>
        </div>
        <div class="submit-button">
          <button class="button-style" @click="submitMenu">確認修改</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import ManagerBlock from '../components/ManagerBlock.vue';

export default {
  components: {
    ManagerBlock,
  },
  data() {
    return {
starters: [      
        { name: '鹹派',   quantity: 0},
        { name: '蝦仁派',   quantity: 0},
        { name: '炸雞翅',   quantity: 0},
        { name: '炸薯條',   quantity: 0},
        { name: '炸雞塊',   quantity: 0},
        { name: '烤蔬菜串',   quantity: 0},
        { name: '鹽烤甜椒',   quantity: 0},
      ],
      salads: [
        { name: '凱薩沙拉',   quantity: 0},
        { name: '蒜香炒青菜',   quantity: 0},
        { name: '青椒炒肉絲',   quantity: 0},
        { name: '炒花椰菜',   quantity: 0},
        { name: '高麗菜炒豆皮',   quantity: 0},
      ],
      special_dishes:[
        { name: '火鍋',   quantity: 0},
        { name: '沙茶肉片',   quantity: 0},
        { name: '蒜香肉片',   quantity: 0},
        { name: '糖醋魚',   quantity: 0},
        { name: '香煎魚',   quantity: 0},
        { name: '鹽烤魚',   quantity: 0},
        { name: '漢堡肉',   quantity: 0},
      ],
      drinks:[
        { name: '咖啡',   quantity: 0},
        { name: '紅茶',   quantity: 0},
        { name: '綠茶',   quantity: 0},
        { name: '奶茶',   quantity: 0},
        { name: '可樂',   quantity: 0},
        { name: '汽水',   quantity: 0},
        { name: '水果茶',   quantity: 0},
      ],
      dessert:[
        { name: '布丁',   quantity: 0},
        { name: '蘋果派',   quantity: 0},
        { name: '曲奇餅',   quantity: 0},
        { name: '馬卡龍',   quantity: 0},
        { name: '蛋糕捲',   quantity: 0},
        { name: '杯子蛋糕',  quantity: 0},
        { name: '奶酪蛋糕',  quantity: 0},
      ],
      ice_cream:[
        {name:'巧克力雪糕',  quantity: 0},
        {name:'小美冰淇淋',  quantity: 0},
        {name:'冰淇淋泡芙',  quantity: 0},
      ],
    };
  },
  mounted() {
    this.fetchInventoryData();
  },
  created() {
    // 在 created 生命週期鉤子中發送 GET 請求來取得庫存數據
    this.fetchInventoryData();
  },
  methods: {
    MenuButton() {
      this.$router.push('/');
    },
    MyOrderButton() {
      this.$router.push('/myorder');
    },
    submitMenu() {
      // 創建包含所有食物名稱與對應數量的 JSON 對象
      const food = [
        { category: 'starters', items: this.starters },
        { category: 'salads', items: this.salads },
        { category: 'special_dishes', items: this.special_dishes },
        { category: 'drinks', items: this.drinks },
        { category: 'dessert', items: this.dessert },
        { category: 'ice_cream', items: this.ice_cream },
      ];
      //包裝Json檔
      const jsonData = JSON.stringify({
        table_name:"FoodInventory",
        food
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
    fetchInventoryData() {
      // 發送 GET 請求獲取庫存數據
      fetch('http://127.0.0.1:5000/api?table=food_inventory', {
        method: 'GET',
      })
        .then(response => response.json())
        .then(data => {
          // 處理 API 返回的數據，更新本地數據
          this.updateInventoryData(data);
        })
        .catch(error => {
          console.error('GET 請求失敗:', error);
          window.alert('獲取庫存信息失敗，請稍後重試。');
        });
    },
    updateInventoryData(data) {
      // 根據返回的數據更新本地數據
      // 假設返回的數據格式為 { "status": "success", "data": { "starters": [...], "salads": [...], ... } }
      
      if (data.status === 'success' && data.data) {
        this.starters = data.data.starters || [];
        this.salads = data.data.salads || [];
        this.special_dishes = data.data.special_dishes || [];
        this.drinks = data.data.drinks || [];
        this.dessert = data.data.dessert || [];
        this.ice_cream = data.data.ice_cream || [];
      }else {
        console.error('API 返回的數據格式不正確:', data);
        window.alert('獲取订单信息失敗，請稍後重試。');
      }
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
.myorder-button{
  margin: 1% 1%; /* 上右下左的順序，1% 表示上下留白 1%，左右留白 1% */
  position: absolute;
  top: 0;
  right: 0;
}
.myorder-button-style{
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
.switch-button{
  margin: 1% 1%; /* 上右下左的順序，1% 表示上下留白 1%，左右留白 1% */
  position: absolute;
  top: 6%;
  right: 0;
}
.menu-button-style{
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