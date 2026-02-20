USE defaultdb;

ALTER TABLE students
ADD COLUMN degree VARCHAR(50),
ADD COLUMN status VARCHAR(20),
ADD COLUMN end_year INT,
ADD COLUMN institute_name VARCHAR(150);

select * from students