SELECT DISTINCT v.author_id AS "id"
FROM Views AS v
WHERE v.author_id = viewer_id
ORDER BY v.author_id;