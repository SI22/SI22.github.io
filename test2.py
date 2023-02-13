import sqlite3
import random
import string

# データベースに接続
conn = sqlite3.connect('mydatabase.db')
c = conn.cursor()

# テーブルを作成
c.execute('''CREATE TABLE IF NOT EXISTS questions
             (id TEXT, title TEXT, content TEXT)''')

# IDを自動的に生成する関数
def generate_id():
    # 8桁のランダムな英数字を生成
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# 質問を追加する関数
def add_question(title, content):
    # IDを生成
    question_id = generate_id()
    # データベースに質問を追加
    c.execute("INSERT INTO questions VALUES (?, ?, ?)", (question_id, title, content))
    # コミット
    conn.commit()
    # 生成されたIDを返す
    return question_id
