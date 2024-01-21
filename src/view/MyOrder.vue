<!-- src/view/MyOrder.vue -->
<template>
  <div>
    <div class="page-header">
      <div class="container">
        <div class="row">
          <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
            <div class="page-caption">
              <h2 class="page-title">管理員系統</h2>
              <p>訂 單 系 統</p>
            </div>
            <div class="inventory-button">
              <button class="inventory-button-style" @click="InventoryButton">切換 庫存管理系統</button>
            </div>
            <div class="switch-button">
              <button class="menu-button-style" @click="MenuButton">切換 MENU</button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>訂單編號</th>
            <th>產品名稱</th>
            <!-- 其他欄位，根據你的訂單訊息需求 -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in orders" :key="order.id">
            <td>{{ order.id }}</td>
            <td>{{ order.name }}</td>
            <!-- 其他欄位，根據你的訂單訊息需求 -->
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  </template>
<script>
export default {
  data() {
    return {
      orders: [], // 存放從資料庫中讀取的訂單訊息
      currentTableName: 'menu_item', // 當前數據表
    };
  },
  // 在這裡觸發讀取資料的方法，例如 created 鉤子中調用 fetchOrders
  created() {
    this.fetchOrders(this.currentTableName);
  },
  methods: {
    MenuButton(){
      this.$router.push('/');
    },
    InventoryButton(){
      this.$router.push('/manager')
    },
    fetchOrders(tableName) {
      this.currentTableName = tableName;
      // 發送 GET 請求獲取庫存數據
      fetch(`http://127.0.0.1:5000/api?table=${tableName}`, {
        method: 'GET',
      })
        .then(response => response.json())
        .then(data => {
          console.log('API 返回的數據:', data);
          // 更新 orders
          this.updateOrderData(data);
        })
        .catch(error => {
          console.error('GET 請求失敗:', error);
          window.alert('獲取庫存信息失敗，請稍後重試。');
        });
    },
    updateOrderData(data) {
      // 根據返回的數據更新本地數據
      // 假設返回的數據格式為 { "status": "success", "data": [...] }
      if (data.status === 'success' && Array.isArray(data.data.menu_item)) {
        this.orders = data.data.menu_item || [];
      } else {
        console.error('API 返回的數據格式不正確:', data);
        window.alert('獲取订单信息失敗，請稍後重試。');
      }
    },
  },
};
</script>

<style>
/*控制標題 */
.page-caption {
  text-align: center; /* 將文本水平置中 */
  margin: 0 auto; /* 通過 margin 屬性實現水平居中，0表示上下不留白，auto表示左右自動分配空間 */
  font-size: 24px;
}
.container{
  display: grid;
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
.inventory-button{
  margin: 1% 1%; /* 上右下左的順序，1% 表示上下留白 1%，左右留白 1% */
  position: absolute;
  top: 0;
  right: 0;
}
.inventory-button-style{
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
/* 在這裡設定表格的樣式，根據需要進行調整 */
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}
</style>