-- Solution 1
SELECT u.user_id AS "buyer_id", u.join_date, COALESCE(sub.orders_in_2019, 0) AS "orders_in_2019"
FROM 
Users AS u
LEFT JOIN
(
    SELECT o.buyer_id, COUNT(o.item_id) AS "orders_in_2019"
    FROM Orders AS o
    WHERE o.order_date BETWEEN '2019-01-01' AND '2019-12-31'
    GROUP BY o.buyer_id
) AS sub
ON u.user_id = sub.buyer_id
ORDER BY sub.buyer_id;

-- Solution 2
SELECT u.user_id AS "buyer_id", u.join_date, COUNT(o.item_id) AS "orders_in_2019"
FROM Users AS u
LEFT JOIN Orders AS o
ON u.user_id = o.buyer_id
AND EXTRACT('Year' from o.order_date) = 2019
GROUP BY user_id, u.join_date
ORDER BY u.user_id;