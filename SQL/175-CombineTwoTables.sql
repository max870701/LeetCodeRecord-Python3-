SELECT p.firstName AS firstname, p.lastName AS lastname, a.city, a.state
FROM Person AS p
LEFT JOIN Address AS a
ON a.personId = p.personId;