-- Solution 1
WITH act_freq AS (
    SELECT
        activity,
        COUNT(activity) AS freq
    FROM Friends
    GROUP BY 1
), freq_extremes AS (
    SELECT
        MAX(a.freq) AS max_freq,
        MIN(a.freq) AS min_freq
    FROM act_freq AS a
)

SELECT
    a.name AS activity
FROM Activities AS a
WHERE a.name NOT IN (
    SELECT activity
    FROM act_freq
    WHERE freq IN (
        (SELECT max_freq FROM freq_extremes),
        (SELECT min_freq FROM freq_extremes)
    )
)

-- Solution 2
WITH act_freq AS (
    SELECT
        activity,
        COUNT(activity) AS freq
    FROM Friends
    GROUP BY 1
)

SELECT DISTINCT activity
FROM Friends
GROUP BY activity
HAVING COUNT(activity) != (SELECT MAX(freq) FROM act_freq)
AND COUNT(activity) != (SELECT MIN(freq) FROM act_freq)