SELECT e.employee_id, sub.team_size
FROM Employee AS e
INNER JOIN
(
    SELECT team_id, COUNT(employee_id) AS "team_size"
    FROM Employee
    GROUP BY team_id
) AS sub
ON e.team_id = sub.team_id;