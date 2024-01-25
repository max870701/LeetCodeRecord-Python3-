SELECT
    MIN(log_id) AS start_id,
    MAX(log_id) AS end_id
FROM (
    SELECT
        ROW_NUMBER() OVER (ORDER BY log_id ASC) AS index,
        log_id
    FROM Logs
) AS sub
GROUP BY log_id - index
ORDER BY start_id;