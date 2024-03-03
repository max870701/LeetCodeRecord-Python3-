WITH first_last_sale AS (
    SELECT
        product_id,
        MIN(sale_date) AS first_sale_date,
        MAX(sale_date) AS last_sale_date
    FROM Sales
    GROUP BY 1
)

SELECT
    f.product_id,
    p.product_name
FROM first_last_sale AS f
LEFT JOIN Product AS p
ON f.product_id = p.product_id
WHERE (first_sale_date BETWEEN '2019-01-01' AND '2019-03-31')
AND (last_sale_date BETWEEN '2019-01-01' AND '2019-03-31')