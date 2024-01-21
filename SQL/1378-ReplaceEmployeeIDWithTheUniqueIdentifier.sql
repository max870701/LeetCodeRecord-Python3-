SELECT uni.unique_id, e.name
FROM EmployeeUNI AS uni
RIGHT JOIN Employees AS e
ON e.id = uni.id;