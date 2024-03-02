-- Solution 1
WITH tiv_2015_duplicates AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
),
unique_locations AS (
    SELECT *
    FROM Insurance AS i
    INNER JOIN (
        SELECT lat, lon
        FROM Insurance
        GROUP BY lat, lon
        HAVING COUNT(*) = 1
    ) AS d
    ON i.lat = d.lat AND i.lon = d.lon
)

SELECT ROUND(SUM(u.tiv_2016)::NUMERIC, 2) AS tiv_2016
FROM unique_locations AS u
JOIN tiv_2015_duplicates AS t ON u.tiv_2015 = t.tiv_2015

-- Solution 2
SELECT ROUND(SUM(d.tiv_2016::NUMERIC), 2) AS tiv_2016
FROM (
    SELECT
        tiv_2016,
        COUNT(*) OVER(PARTITION BY tiv_2015) AS count_tiv_2015,
        COUNT(*) OVER(PARTITION BY lat, lon) AS count_lat_lon
    FROM Insurance
) AS d
WHERE d.count_tiv_2015 > 1 AND d.count_lat_lon = 1