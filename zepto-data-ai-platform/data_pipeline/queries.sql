-- 1. Select all books with rating >= 4
SELECT title, rating FROM books WHERE rating >= 4;

-- 2. List top 10 most expensive books
SELECT title, price_gbp FROM books ORDER BY price_gbp DESC LIMIT 10;

-- 3. Distinct categories
SELECT DISTINCT name FROM categories;

-- 4. Books priced between 20 and 30 GBP
SELECT title, price_gbp FROM books WHERE price_gbp BETWEEN 20 AND 30;

-- 5. Join books with categories
SELECT b.title, c.name, b.rating
FROM books b
JOIN categories c ON b.category_id = c.id
ORDER BY c.name, b.rating DESC;
