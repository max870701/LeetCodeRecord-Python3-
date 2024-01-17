SELECT sub.customer_number
FROM
(
    SELECT o.customer_number, COUNT(o.customer_number) AS "count"
    FROM Orders AS o
    GROUP BY o.customer_number
    ORDER BY "count" DESC
) AS sub
LIMIT 1;