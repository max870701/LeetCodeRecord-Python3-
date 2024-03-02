-- Write your PostgreSQL query statement below
SELECT
    a.player_id,
    a.device_id
FROM (
    SELECT
        player_id,
        device_id,
        DENSE_RANK() OVER(PARTITION BY player_id ORDER BY event_date ASC) AS rank
    FROM Activity
) AS a
WHERE a.rank = 1