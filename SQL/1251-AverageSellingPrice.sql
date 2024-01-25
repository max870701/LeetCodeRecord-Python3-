WITH price_units AS (
    SELECT
        p.product_id,
        p.price,
        u.units
    FROM Prices AS p
    LEFT JOIN UnitsSold AS u
    ON (u.purchase_date BETWEEN p.start_date AND p.end_date)
    AND p.product_id = u.product_id
)

SELECT
    product_id,
    COALESCE(ROUND(SUM(price * units)::NUMERIC / SUM(units), 2), 0) AS average_price
FROM price_units
GROUP BY product_id;