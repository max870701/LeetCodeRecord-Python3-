SELECT
    MIN(ABS(x1-x2)) AS shortest
FROM (
    SELECT p1.x AS x1, p2.x AS x2
    FROM Point AS p1
    CROSS JOIN Point AS p2
    WHERE p1.x != p2.x
);