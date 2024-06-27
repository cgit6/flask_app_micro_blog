from flask import Flask, request
from flask import render_template, redirect
import datetime as d
from pymongo import MongoClient


def create_app():
    app = Flask(__name__)
    # 連上 Cluster0
    client = MongoClient("mongodb+srv://sean:ZNaZYH93Rj4jNXXH@cluster0.4oxtimq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    # 連上數據庫
    app.db = client.microblog


    # 存放資料的地方 
    entries = []

    @app.route("/", methods=["GET","POST"])
    def home():
        print([e for e in app.db.entries.find({})]) # 所有資料
        # 獲取資料
        if request.method == "POST":
            entry_content = request.form.get("content") # 這個 content 是 textarea 的 name 屬性
            formatted_date = d.datetime.today().strftime("%Y-%m-%d") # 這個是 string
            # print(entry_content,formatted_date)
            # entries.append((entry_content, formatted_date))

            # 新增資料到資料庫
            app.db.entries.insert_one({"content": entry_content, "date":formatted_date})

        # 更新畫面
        # 調整時間格式
        # 列表生成式
        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                # 這個資料個是是date
                d.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d"), 
            )
            for entry in app.db.entries.find({}) # 對於 `entries` 中的每個條目 `entry`
        ]
        return render_template("app.html", entries = entries_with_date)

    @app.route("/md")
    def index():
        return render_template('md.html')

    # @app.route('/entry', methods=['POST'])
    # def add_entry():
    #     content = request.form['content']
    #     # 在這裡處理你的表單數據，例如將其保存到數據庫中
    #     return redirect(url_for('app'))

    return app

# if __name__ == '__main__':
#     app.create_app(debug=True)