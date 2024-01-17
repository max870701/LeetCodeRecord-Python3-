SELECT MAX(sub.num) AS "num"
FROM
(
    SELECT m.num, COUNT(m.num) AS "count"
    FROM MyNumbers AS m
    GROUP BY m.num
) AS sub
WHERE sub.count = 1;