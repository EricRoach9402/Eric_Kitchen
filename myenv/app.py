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

class MenuItem(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(255), nullable=False)

# 在這裡建立應用程式上下文
with app.app_context():
     # 建立資料庫表
     db.create_all()

class ReceiveDataResource(Resource):
     def get(self):
         return {'message': 'GET method is not allowed on this endpoint'}, 405

     def post(self):
         try:
             #取得完整Json檔
             data = request.get_json()
             #特別注意，「name=」是指資料庫中的name欄位，而data.get中的name則是指json檔中name屬性的資料
             item = MenuItem(name=data.get('name', ''))
             #將資料提交至session表示為欲上傳資料
             db.session.add(item)
             #進行上傳
             db.session.commit()

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