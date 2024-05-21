from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def init_db():
    conn = sqlite3.connect('registration.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        role TEXT NOT NULL,
        student_id TEXT,
        course TEXT,
        teacher_id TEXT,
        subject TEXT
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    role = 'student' if 'studentId' in request.form else 'teacher'
    student_id = request.form.get('studentId')
    course = request.form.get('course')
    teacher_id = request.form.get('teacherId')
    subject = request.form.get('subject')

    conn = sqlite3.connect('registration.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (name, email, role, student_id, course, teacher_id, subject)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (name, email, role, student_id, course, teacher_id, subject))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
