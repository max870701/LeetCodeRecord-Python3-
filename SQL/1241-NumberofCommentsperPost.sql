WITH tmp AS (
    SELECT
        DISTINCT ON (parent_id, sub_id)
        parent_id,
        sub_id
    FROM Submissions
    WHERE parent_id IS NOT NULL
    GROUP BY parent_id, sub_id
), main AS (
    SELECT DISTINCT sub_id AS "post_id"
    FROM Submissions
    WHERE parent_id IS NULL
)


SELECT m.post_id, COALESCE(sub.num, 0) AS "number_of_comments"
FROM main AS m
LEFT JOIN (
    SELECT parent_id, COUNT(sub_id) AS "num"
    FROM tmp
    GROUP BY parent_id
) AS sub
ON m.post_id = sub.parent_id
ORDER BY m.post_id;