from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # 引入 CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0000@localhost/Menu_SQL'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
api = Api(app)
CORS(app)

# 定義 MenuItem 資料表
class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

# 定義 FoodInventory 資料表
class FoodInventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    

# 在這裡建立應用程式上下文
with app.app_context():
    # 建立資料庫表
    db.create_all()

class ReceiveDataResource(Resource):
    def get(self):
        try:
            # 獲取庫存數據
            inventory_data = self.get_inventory_data()
            if inventory_data == {'starters': [], 'salads': [], 'special_dishes': [], 'drinks': [], 'dessert': [], 'ice_cream': []}:
                return {"status": "error", "message": "庫存數據為空"}, 500
            response_data = {
                "status": "success",
                "data": inventory_data,
            }
            return response_data, 200
        except Exception as e:
            print("Error processing GET request:", str(e))
            return {"status": "error", "message": "Error processing GET request"}, 500
    def get_inventory_data(self):
        # 這裡根據你的需求從資料庫中獲取庫存數據
        # 假設你有一個函數可以從 FoodInventory 資料表中獲取數據，你可以像這樣調用：
        starters = self.get_category_inventory('starters')
        salads = self.get_category_inventory('salads')
        special_dishes = self.get_category_inventory('special_dishes')
        drinks = self.get_category_inventory('drinks')
        dessert = self.get_category_inventory('dessert')
        ice_cream = self.get_category_inventory('ice_cream')

        return {
            "starters": starters,
            "salads": salads,
            "special_dishes": special_dishes,
            "drinks": drinks,
            "dessert": dessert,
            "ice_cream": ice_cream,
        }

    def get_category_inventory(self, category):
        # 直接從資料庫中獲取指定類別的庫存數據
        inventory_data = FoodInventory.query.filter_by(category=category).all()

        # 將庫存數據轉換為字典格式
        result = [{"name": item.name, "quantity": item.quantity} for item in inventory_data]

        return result

    def post(self):
        try:
            # 取得完整 JSON 檔
            data = request.get_json()

            # 取得要更新的資料表名稱
            table_name = data.get('table_name', '')

            if table_name == 'MenuItem':
                # 建立 MenuItem 資料
                print("收到MenuItem")
                item = MenuItem(name=data.get('name', ''))
                # 將資料提交至 session 表示為欲上傳資料
                db.session.add(item)
                # 在這裡執行 db.session.commit()
                db.session.commit()
            elif table_name == 'FoodInventory':
                # 更新 FoodInventory 資料
                for category_data in data.get('food', []):
                    category_name = category_data.get('category', '')
                    for food_item in category_data.get('items', []):
                        food_name = food_item.get('name', '')
                        food_quantity = food_item.get('quantity', 0)

                        # 查詢是否已存在該食物資料，若不存在則新增，存在則更新數量
                        existing_food = FoodInventory.query.filter_by(category=category_name, name=food_name).first()
                        if existing_food:
                            existing_food.quantity = int(food_quantity)
                        else:
                            new_food = FoodInventory(category=category_name, name=food_name, quantity=food_quantity)
                            db.session.add(new_food)
                # 在這裡執行 db.session.commit()
                db.session.commit()
            else:
                return {"status": "error", "message": "Invalid table_name provided"}, 400
            response_data = {
                "status": "success",
                "message": f"Data received and stored successfully: {data}"
            }
            return response_data, 200
        except Exception as e:
            print("Error processing request:", str(e))
            return {"status": "error", "message": "Error processing request"}, 500

api.add_resource(ReceiveDataResource, '/api')

if __name__ == "__main__":
    app.run(debug=False)
