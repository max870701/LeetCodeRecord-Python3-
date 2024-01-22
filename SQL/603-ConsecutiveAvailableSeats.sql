SELECT seat_id
FROM
(
    SELECT
        seat_id,
        free,
        LEAD(free, 1) OVER(ORDER BY seat_id) AS free_lead,
        LAG(free, 1) OVER(ORDER BY seat_id) AS free_lag
    FROM Cinema
)
WHERE (free = 1 AND free_lead = 1)
OR (free = 1 AND free_lag = 1);