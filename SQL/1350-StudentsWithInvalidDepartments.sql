SELECT s.id, s.name
FROM Students AS s
LEFT JOIN Departments AS d
ON s.department_id = d.id
WHERE d.name IS NULL;