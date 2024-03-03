-- Write your PostgreSQL query statement below
WITH customer_id_order AS (
    SELECT
        customer_id,
        order_date,
        customer_pref_delivery_date,
        ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY order_date) AS rn
    FROM Delivery
)

SELECT
    ROUND(COUNT(
        CASE
            WHEN order_date = customer_pref_delivery_date THEN 1
        END
    ) * 100.0 / COUNT(customer_id), 2) AS immediate_percentage
FROM customer_id_order
WHERE rn = 1