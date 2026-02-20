from flask import Flask, render_template, request, redirect, url_for
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# --- Database Connection (Cloud Ready) ---
def get_db_connection():
    try:
        return pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT")), # Port must be a number!
            cursorclass=pymysql.cursors.DictCursor
        )
    except Exception as err:
        print(f"❌ DATABASE ERROR: {err}")
        return None
    
# --- Routes ---
@app.route('/')
def index():
    conn = get_db_connection()
    if conn is None:
        return "<h1>❌ Error: Could not connect to MySQL. Check your password in .env</h1>"
    
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
    conn.close()
    
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    if request.method == 'POST':
        # Grab old and new data from the form
        name = request.form['name']
        dept = request.form['dept']
        year = request.form['year']
        cgpa = request.form['cgpa']
        institute_name = request.form['institute_name']
        degree = request.form['degree']
        status = request.form['status']
        end_year = request.form['end_year']

        conn = get_db_connection()
        if conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO students 
                       (name, department, year_of_study, cgpa, institute_name, degree, status, end_year) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", 
                    (name, dept, year, cgpa, institute_name, degree, status, end_year)
                )
            conn.commit()
            conn.close()
        return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_student(id):
    conn = get_db_connection()
    if conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM students WHERE id = %s", (id,))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
        student = cursor.fetchone()
        conn.close()
        if student:
            return render_template('edit.html', student=student)
        return "Student not found", 404

    if request.method == 'POST':
        # Grab updated data
        name = request.form['name']
        dept = request.form['dept']
        year = request.form['year']
        cgpa = request.form['cgpa']
        institute_name = request.form['institute_name']
        degree = request.form['degree']
        status = request.form['status']
        end_year = request.form['end_year']

        cursor.execute(
            """UPDATE students 
               SET name=%s, department=%s, year_of_study=%s, cgpa=%s, 
                   institute_name=%s, degree=%s, status=%s, end_year=%s 
               WHERE id=%s""",
            (name, dept, year, cgpa, institute_name, degree, status, end_year, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

if __name__ == '__main__':
    print("--- 🚀 STARTING STUDENT MANAGER (PyMySQL Mode) ---")
    print("--- Go to http://127.0.0.1:5000 in your browser ---")
    app.run(debug=True, use_reloader=False, port=5000)