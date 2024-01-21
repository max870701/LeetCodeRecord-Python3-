SELECT p.product_name, sub.total_unit AS unit
FROM Products AS p
LEFT JOIN
(
    SELECT product_id, SUM(unit) AS total_unit
    FROM Orders
    WHERE TO_CHAR(order_date, 'YYYY-MM') = '2020-02'
    GROUP BY product_id
) AS sub
ON p.product_id = sub.product_id
WHERE sub.total_unit >= 100;