-- Write your PostgreSQL query statement below
WITH RECURSIVE EmployeeHierarchy AS (
    -- 基本案例：直接報告給特定經理（employee_id = 1）的員工
    SELECT employee_id, manager_id
    FROM Employees
    WHERE manager_id = 1 AND employee_id != 1
    UNION ALL
    -- 遞迴部分：尋找每個員工的下屬員工
    SELECT e.employee_id, e.manager_id
    FROM Employees e
    INNER JOIN EmployeeHierarchy eh ON e.manager_id = eh.employee_id
)
SELECT employee_id
FROM EmployeeHierarchy;