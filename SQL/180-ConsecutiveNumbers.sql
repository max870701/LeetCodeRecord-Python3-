-- Solution 1
WITH t1 AS (
    SELECT l1.id, l1.num, l2.num AS "num2"
    FROM Logs AS l1
    INNER JOIN Logs AS l2
    ON l1.id = l2.id - 1
), t2 AS (
    SELECT t1.id, t1.num, t1.num2, l3.num AS "num3"
    FROM t1 
    INNER JOIN Logs AS l3
    ON t1.id = l3.id - 2
)

SELECT DISTINCT t2.num AS "ConsecutiveNums"
FROM t2
WHERE t2.num = t2.num2 AND t2.num2 = t2.num3;

-- Solution 2
SELECT DISTINCT l1.num AS "ConsecutiveNums"
FROM Logs l1, Logs l2, Logs l3
WHERE
    l1.id = l2.id - 1 AND
    l2.id = l3.id - 1 AND
    l1.num = l2.num AND
    l2.num = l3.num;

-- Solution 3
SELECT DISTINCT num AS "ConsecutiveNums"
FROM (
    SELECT num,
           LEAD(num) OVER (ORDER BY id) AS next_num,
           LEAD(num, 2) OVER (ORDER BY id) AS next_next_num
    FROM Logs
) subquery
WHERE num = next_num AND next_num = next_next_num;