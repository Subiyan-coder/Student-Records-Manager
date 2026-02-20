# 🎓 Student Records Manager

[![Live Demo](https://img.shields.io/badge/Live_Demo-Click_Here-05192D?style=for-the-badge&logo=render)]https://student-records-manager-50un.onrender.com/)

A lightweight, web-based CRUD (Create, Read, Update, Delete) application designed to manage student data. This project demonstrates backend database integration using Python and MySQL, served through a modern web interface.

![Student Manager Web App](images/app-screenshot.png)

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Database:** MySQL (using `PyMySQL` driver)
* **Frontend:** HTML5, Bootstrap 5 (via CDN)
* **Environment Management:** `python-dotenv` for secure credential handling

## ✨ Features

* **Full CRUD Operations:** Seamlessly Create, Read, Update, and Delete student records.
* **Comprehensive Data Tracking:** Manage detailed academic profiles, including:
  * Full Name & Institute Name
  * Degree & Department
  * Current Academic Status (Pursuing / Completed) & Expected End Year
  * Current Year of Study & CGPA
* **Cloud Database Integration:** Securely connected to a live MySQL database hosted on Aiven.
* **Production Deployment:** Fully hosted and accessible online via Render with a Gunicorn WSGI server.
* **Responsive UI:** Clean, modern, and user-friendly web interface styled with Bootstrap.

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
