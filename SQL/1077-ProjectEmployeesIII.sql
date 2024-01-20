WITH pid_exp AS (
    SELECT p.project_id, e.employee_id, e.experience_years
    FROM Project AS p
    INNER JOIN Employee AS e
    ON p.employee_id = e.employee_id
)

SELECT project_id, employee_id 
FROM pid_exp
WHERE (project_id, experience_years) IN (
    SELECT project_id, MAX(experience_years) AS "max_experience"
    FROM pid_exp
    GROUP BY project_id
);