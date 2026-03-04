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
            port=int(os.getenv("DB_PORT")), 
            cursorclass=pymysql.cursors.DictCursor
        )
    except Exception as err:
        print(f"❌ DATABASE ERROR: {err}")
        return None

# --- NEW: Health Check Route for Cron Job ---
@app.route('/health')
def health_check():
    # Render returns this instantly to cron-job.org without hitting the Aiven database!
    return "OK", 200

# --- Routes ---
@app.route('/')
def index():
    conn = get_db_connection()
    if conn is None:
        return "<h1>❌ Error: Could not connect to MySQL. Check your password in .env</h1>"
    
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()
    finally:
        # This guarantees the connection closes EVEN IF an error happens above
        conn.close()
    
    return render_template('index.html', students=students)

@app.route('/add', methods=['POST'])
def add_student():
    if request.method == 'POST':
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
            try:
                with conn.cursor() as cursor:
                    cursor.execute(
                        """INSERT INTO students 
                           (name, department, year_of_study, cgpa, institute_name, degree, status, end_year) 
                           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", 
                        (name, dept, year, cgpa, institute_name, degree, status, end_year)
                    )
                conn.commit()
            finally:
                conn.close()
                
        return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_student(id):
    conn = get_db_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM students WHERE id = %s", (id,))
            conn.commit()
        finally:
            conn.close()
            
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    conn = get_db_connection()
    if not conn:
        return "<h1>Database connection failed.</h1>", 500

    try:
        if request.method == 'GET':
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
                student = cursor.fetchone()
            if student:
                return render_template('edit.html', student=student)
            return "Student not found", 404

        if request.method == 'POST':
            name = request.form['name']
            dept = request.form['dept']
            year = request.form['year']
            cgpa = request.form['cgpa']
            institute_name = request.form['institute_name']
            degree = request.form['degree']
            status = request.form['status']
            end_year = request.form['end_year']

            with conn.cursor() as cursor:
                cursor.execute(
                    """UPDATE students 
                       SET name=%s, department=%s, year_of_study=%s, cgpa=%s, 
                           institute_name=%s, degree=%s, status=%s, end_year=%s 
                       WHERE id=%s""",
                    (name, dept, year, cgpa, institute_name, degree, status, end_year, id)
                )
            conn.commit()
            return redirect(url_for('index'))
            
    finally:
        conn.close()

if __name__ == '__main__':
    print("--- 🚀 STARTING STUDENT MANAGER (PyMySQL Mode) ---")
    print("--- Go to http://127.0.0.1:5000 in your browser ---")
    app.run(debug=True, use_reloader=False, port=5000)