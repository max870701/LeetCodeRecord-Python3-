-- Solution 1
SELECT s.buyer_id
FROM Sales AS s
INNER JOIN Product AS p
ON s.product_id = p.product_id
GROUP BY s.buyer_id
HAVING
    SUM(CASE WHEN p.product_name = 'S8' THEN 1 ELSE 0 END) >= 1
AND
    SUM(CASE WHEN p.product_name = 'iPhone' THEN 1 ELSE 0 END) = 0;

-- Solution 2
WITH s8_buyers AS (
    SELECT buyer_id
    FROM Sales AS s
    JOIN Product AS p
    ON s.product_id = p.product_id
    WHERE product_name = 'S8'
), iphone_buyers AS (
    SELECT buyer_id
    FROM Sales AS s
    JOIN Product AS p
    ON s.product_id = p.product_id
    WHERE product_name = 'iPhone'
)

SELECT DISTINCT buyer_id
FROM Sales AS s
WHERE s.buyer_id IN (SELECT buyer_id FROM s8_buyers)
AND s.buyer_id NOT IN (SELECT buyer_id FROM iphone_buyers);