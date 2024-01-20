SELECT s.product_id, sub.first_year, s.quantity, s.price
FROM 
(
    SELECT product_id, MIN(year) AS "first_year"
    FROM Sales
    GROUP BY product_id
) AS sub
RIGHT JOIN Sales AS s
ON sub.product_id = s.product_id
WHERE s.year = sub.first_year;