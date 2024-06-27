from flask import Flask, request
from flask import render_template, redirect
import datetime as d
app = Flask(__name__)

# 存放資料的地方 
entries = []

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        entry_content = request.form.get("content") # 這個 content 是 textarea 的 name 屬性
        formatted_date = d.datetime.today().strftime("%Y-%m-%d") # 這個是 string
        # print(entry_content,formatted_date)
        entries.append((entry_content, formatted_date))
    
    # 調整時間格式
    entries_with_date = [
        (
            entry[0],
            entry[1],
            d.datetime.strptime(entry[1], "%Y-%m-%d").strftime("%b %d"), # 這個資料個是是date
        ) 
        for entry in entries:
            pass
    ]

    return render_template("app.html", entries = entries)

@app.route('/md')
def index():
    return render_template('md.html')

# @app.route('/entry', methods=['POST'])
# def add_entry():
#     content = request.form['content']
#     # 在這裡處理你的表單數據，例如將其保存到數據庫中
#     return redirect(url_for('app'))

if __name__ == '__main__':
    app.run(debug=True)