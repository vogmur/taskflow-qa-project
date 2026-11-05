from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

#Функция для подключения к БД
def get_db_connection():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

#Создаем таблицу при первом запуске
with app.app_context():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, status TEXT DEFAULT "todo")')
    conn.close()

# 1. Отдаем HTML страницу
@app.route('/')
def index():
    return render_template('index.html')

# 2. API: Получить все задачи (GET)
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return jsonify([dict(task) for task in tasks])

# 3. API: Создать задачу (POST)
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data or data ['title'].strip() == '':
        return jsonify({"error": "Title is required"}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO tasks (title) VALUES (?)', (data['title'],))
    conn.commit()
    conn.close()
    return jsonify({"message": "Task created"}), 201

if __name__ == '__main__':
    app.run(debug=True)

