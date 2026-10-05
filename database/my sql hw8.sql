-- 1. Create the database
CREATE DATABASE BookStoreDB;

-- 2. Select the database
USE BookStoreDB;

-- 3. Create the authors table
CREATE TABLE authors (
    author_id INT PRIMARY KEY,
    name VARCHAR(100),
    country VARCHAR(100)
);

-- 4. Create the books table
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200),
    price DECIMAL(10,2),
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- 5. Add published_year to books
ALTER TABLE books
ADD published_year INT;

-- 6. Add some authors
INSERT INTO authors
(author_id, name, country)
VALUES
(1, 'George Orwell', 'United Kingdom'),
(2, 'J.K. Rowling', 'United Kingdom'),
(3, 'R.K. Narayan', 'India');

-- 7. Add some books
INSERT INTO books
(book_id, title, price, author_id, published_year)
VALUES
(1, '1984', 399.00, 1, 1949),
(2, 'Harry Potter and the Philosopher''s Stone', 499.00, 2, 1997),
(3, 'Malgudi Days', 299.00, 3, 1943);

-- 8. Display authors
SELECT *
FROM authors;

-- 9. Display books
SELECT *
FROM books;

-- 10. Delete all rows from books
DELETE FROM books;

-- 11. Delete the entire database
DROP DATABASE BookStoreDB;