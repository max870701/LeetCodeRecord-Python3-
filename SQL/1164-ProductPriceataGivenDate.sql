-- Solution 1
WITH latest_change AS (
    SELECT product_id, MAX(change_date) AS "latest_change_date"
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)

SELECT DISTINCT p.product_id,
    (CASE
        WHEN l.latest_change_date IS NULL THEN 10
        ELSE p.new_price
    END) AS "price"
FROM Products AS p
LEFT JOIN latest_change AS l
ON p.product_id = l.product_id
WHERE p.change_date = l.latest_change_date
OR l.latest_change_date IS NULL;

-- Solution 2
WITH latest_price AS (
    SELECT
        DISTINCT ON (product_id)
        product_id, new_price
    FROM Products
    WHERE change_date <= '2019-08-16'
    ORDER BY product_id ASC, change_date DESC
)

SELECT p.product_id, COALESCE(l.new_price, 10) AS "price"
FROM (SELECT DISTINCT product_id FROM Products) AS p
LEFT JOIN latest_price AS l
USING (product_id);