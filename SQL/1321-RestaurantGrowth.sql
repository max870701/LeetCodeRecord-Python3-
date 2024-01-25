WITH DailyTotal AS (
    SELECT
        visited_on,
        SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
    ORDER BY visited_on
), AccumulatedTotal AS (
    SELECT
        visited_on,
        SUM(daily_amount) OVER(ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS accumulated_amount
    FROM DailyTotal
)


SELECT
    visited_on,
    accumulated_amount AS amount,
    ROUND(accumulated_amount / 7.0, 2) AS average_amount
FROM AccumulatedTotal
WHERE visited_on >= (
    SELECT visited_on
    FROM DailyTotal
    LIMIT 1
) + INTERVAL '6 day';