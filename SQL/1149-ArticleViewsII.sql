-- Solution 1
SELECT DISTINCT sub.viewer_id AS "id"
FROM
(
    SELECT view_date, viewer_id, COUNT(DISTINCT article_id)
    FROM Views
    GROUP BY view_date, viewer_id
) AS sub
WHERE sub.count > 1
ORDER BY sub.viewer_id;

-- Solution 2
SELECT DISTINCT viewer_id AS "id"
FROM Views
GROUP BY viewer_id, view_date
HAVING COUNT(DISTINCT article_id) > 1;