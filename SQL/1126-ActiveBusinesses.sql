SELECT e.business_id
FROM Events AS e
INNER JOIN
(
    SELECT
        event_type,
        AVG(occurrences) AS average_activity
    FROM Events
    GROUP BY event_type
) AS sub
ON e.event_type = sub.event_type
WHERE e.occurrences > sub.average_activity
GROUP BY 1
HAVING COUNT(e.business_id) > 1;