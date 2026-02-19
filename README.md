# 🎓 Student Records Manager

A lightweight, web-based CRUD (Create, Read, Update, Delete) application designed to manage student data. This project demonstrates backend database integration using Python and MySQL, served through a modern web interface.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Database:** MySQL (using `PyMySQL` driver)
* **Frontend:** HTML5, Bootstrap 5 (via CDN)
* **Environment Management:** `python-dotenv` for secure credential handling

## ✨ Features
* **Create:** Add new students with their Name, Department, Year of Study, and CGPA.
* **Read:** View a formatted table of all enrolled students.
* **Update:** Edit existing student details and dynamically update the database.
* **Delete:** Remove a student record from the system.

## 🚀 Setup & Installation

### Prerequisites
* Python 3.x installed
* MySQL Server installed and running

1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/Student-Records-Manager.git](https://github.com/YOUR_USERNAME/Student-Records-Manager.git)
cd Student-Records-Manager

2. Database Setup
Open MySQL Workbench (or your preferred SQL client).

Execute the database_setup.sql file provided in this repository to create the student_db database and the students table.

3. Install Dependencies
Install the required Python libraries using pip:

Bash
pip install -r requirements.txt
4. Environment Variables
Create a file named .env in the root directory of the project. Add your MySQL root password to it:

Code snippet
DB_PASSWORD=your_actual_mysql_password_here
(Note: The .env file is included in .gitignore and will not be pushed to version control.)

5. Run the Application
Start the Flask development server:

Bash
python app.py
Open your web browser and navigate to http://127.0.0.1:5000 to view the application.

👨‍💻 Author
Mohamed Muneerul Subiyan.R


### Next Steps to Finalize
You will need to change `YOUR_USERNAME` in the clone link to your actual GitHub username. 
