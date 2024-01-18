-- Solution1
SELECT d.name AS "Department", e.name AS "Employee", e.salary AS "Salary"
FROM Employee AS e
INNER JOIN Department AS d ON e.departmentId = d.id
INNER JOIN
(
    SELECT departmentId, MAX(salary) AS "max_salary"
    FROM Employee
    GROUP BY departmentId
) AS sub
ON e.departmentId = sub.departmentId
WHERE sub.max_salary = e.salary;

-- Solution2
SELECT d.name AS "Department", e.name AS "Employee", e.salary AS "Salary"
FROM Employee AS e, Department AS d
WHERE e.departmentId = d.id
AND (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);