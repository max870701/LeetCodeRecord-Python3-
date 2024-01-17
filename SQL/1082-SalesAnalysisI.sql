-- Solution 1
WITH seller_sales AS (
    SELECT s.seller_id, SUM(s.price) AS sales_amount
    FROM Sales AS s
    GROUP BY s.seller_id
    ORDER BY sales_amount DESC, s.seller_id
)

SELECT t1.seller_id
FROM seller_sales AS t1
WHERE t1.sales_amount = (
    SELECT MAX(t2.sales_amount)
    FROM seller_sales AS t2
);
-- Solution 2
SELECT s.seller_id
FROM Sales AS s
GROUP BY s.seller_id
HAVING SUM(s.price) = (
    SELECT SUM(s2.price)
    FROM Sales AS s2
    GROUP BY s2.seller_id
    ORDER BY 1 DESC
    LIMIT 1
);