CREATE DATABASE college;

USE college;

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(100),
    grade INT
);

INSERT INTO students (id, name, age, department, grade)
VALUES
(1, 'Arjun', 21, 'Computer Science', 90),
(2, 'Rahul', 19, 'Physics', 78),
(3, 'Ananya', 22, 'Mathematics', 85),
(4, 'Meera', 20, 'Computer Science', 72);

SELECT *
FROM students
WHERE age > 20;

SELECT *
FROM students
WHERE department = 'Computer Science'
   OR department = 'Physics';

SELECT *
FROM students
WHERE grade = 90;

SELECT *
FROM students
WHERE grade BETWEEN 70 AND 90;