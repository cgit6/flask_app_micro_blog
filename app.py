from flask import Flask, request
from flask import render_template, redirect
import datetime 
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    # 連上 Cluster0
    client = MongoClient(os.getenv("MONGODB_URI"))
    # 連上數據庫
    app.db = client.microblog

    # 存放資料的地方 
    # entries = []


    @app.route("/", methods=["GET", "POST"])
    def home():
        # 如果是 POST 方法
        # print([e for e in app.db.entries.find({})]) # 所有資料
        # 獲取資料
        if request.method == "POST":
            # 這個 content 是 textarea 的 name 屬性
            entry_content = request.form.get("content") 
            # 這個是 string，
            # strftime() 是 datetime 對象的方法，用於將日期和時間格式化為指定的字符串格式。
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d") 
            # print(entry_content,formatted_date)
            # entries.append((entry_content, formatted_date))

            # 新增資料到資料庫
            app.db.entries.insert_one({"content": entry_content, "date":formatted_date})

        # 如果是 GET 方法
        # 更新畫面，列出文章結果
        # 調整時間格式
        # 列表生成式
        entries_with_date = [
            (
                entry["content"],
                entry["date"],
                # 這個資料個是是date
                # strptime 將符合格式的字串轉換為時間資料型態
                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d"), 
            )
            # 對每一筆儲存在 mongodb 的資料做...
            for entry in app.db.entries.find({}) # 對於 `entries` 中的每個條目 `entry`
        ]
        print(entries_with_date)
        return render_template("app.html", entries = entries_with_date)

    # # 試著建立 markdown 頁面
    # @app.route("/md")
    # def index():
    #     return render_template("md.html")

    # @app.route('/entry', methods=['POST'])
    # def add_entry():
    #     content = request.form['content']
    #     # 在這裡處理你的表單數據，例如將其保存到數據庫中
    #     return redirect(url_for('app'))

    return app