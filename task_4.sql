-- Use the correct database
USE alx_book_store;

-- Display the full description of the 'books' table without using DESCRIBE or EXPLAIN
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Books'
  AND TABLE_SCHEMA = 'alx_book_store';
