SELECT p1.project_id
FROM Project AS p1
GROUP BY p1.project_id
HAVING COUNT(p1.employee_id) = (
    SELECT MAX(sub.employee_number)
    FROM (
        SELECT COUNT(p2.employee_id) AS "employee_number"
        FROM Project AS p2
        GROUP BY p2.project_id
    ) AS sub
)
ORDER BY p1.project_id;