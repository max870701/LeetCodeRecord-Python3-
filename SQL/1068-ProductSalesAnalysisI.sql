SELECT p.product_name, s.year, s.price
FROM Sales AS s
JOIN Product AS p
ON s.product_id = p.product_id
ORDER BY p.product_name;