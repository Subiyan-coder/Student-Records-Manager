CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    year_of_study INT,
    cgpa DECIMAL(3, 2)
);

INSERT INTO students (name, department, year_of_study, cgpa) 
VALUES ('Test Student', 'CS', 1, 8.5);