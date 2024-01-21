-- Solution 1
WITH avg AS (
    SELECT c.country_name, ROUND(AVG(w.weather_state), 2) AS "avg_temp"
    FROM Weather AS w
    INNER JOIN Countries AS c
    ON w.country_id = c.country_id
    WHERE TO_CHAR(w.day, 'YYYY-MM') = '2019-11'
    GROUP BY c.country_name
)

SELECT
    country_name,
    CASE
        WHEN avg_temp >= 25 THEN 'Hot'
        WHEN avg_temp <= 15 THEN 'Cold'
        ELSE 'Warm'
    END AS "weather_type"
FROM avg;

-- Solution 2
SELECT
    c.country_name,
    CASE
        WHEN AVG(w.weather_state) >= 25 THEN 'Hot'
        WHEN AVG(w.weather_state)  <= 15 THEN 'Cold'
        ELSE 'Warm'
    END AS "weather_type"
FROM Weather AS w
INNER JOIN Countries AS c
ON w.country_id = c.country_id
WHERE TO_CHAR(w.day, 'YYYY-MM') = '2019-11'
GROUP BY c.country_name;