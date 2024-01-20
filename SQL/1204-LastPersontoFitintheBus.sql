-- Solution 1
WITH total_weight AS
(
    SELECT q.turn, q.person_name, SUM(q.weight) OVER (ORDER BY q.turn) AS "total"
    FROM Queue AS q
)

SELECT t.person_name
FROM total_weight AS t
WHERE 1000 - t.total >= 0
ORDER BY t.turn DESC
LIMIT 1;

-- Solution 2
SELECT q1.person_name
FROM Queue q1
JOIN Queue q2
ON q1.turn >= q2.turn
GROUP BY q1.person_id, q1.person_name
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1;