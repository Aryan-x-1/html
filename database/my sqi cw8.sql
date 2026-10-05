-- Create database
CREATE DATABASE GroceryShop;

-- Select database
USE GroceryShop;

-- Create products table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);

-- Add category column
ALTER TABLE products
ADD category VARCHAR(100);

-- Insert some products
INSERT INTO products
(product_id, product_name, price, category)
VALUES
(1, 'Rice', 60.00, 'Grains'),
(2, 'Milk', 55.00, 'Dairy'),
(3, 'Apple', 120.00, 'Fruits');

-- Display products
SELECT *
FROM products;

-- Remove all rows but keep the table
TRUNCATE TABLE products;

-- Delete the entire database
DROP DATABASE GroceryShop;