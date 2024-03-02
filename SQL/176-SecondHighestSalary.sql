-- Write your PostgreSQL query statement below
SELECT
COALESCE(
(    
    SELECT
        salary
    FROM (
        SELECT
            id,
            salary,
            DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
        FROM Employee
    ) AS "SalaryRank"
    WHERE rank = 2
    LIMIT 1
),
NULL) AS "SecondHighestSalary"