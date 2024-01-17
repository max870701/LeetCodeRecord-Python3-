SELECT p.email AS "Email" 
FROM Person AS p
GROUP BY p.email
HAVING COUNT(p.email) > 1;