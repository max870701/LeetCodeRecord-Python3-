WITH tmp AS
(
    SELECT
        p1.x AS x1,
        p1.y AS y1,
        p2.x AS x2,
        p2.y AS y2
    FROM Point2D AS p1
    CROSS JOIN Point2D AS p2
    WHERE NOT (p1.x = p2.x AND p1.y = p2.y)
)

SELECT
    MIN(ROUND(SQRT(POW(x2-x1, 2) + POW(y2-y1, 2))::NUMERIC, 2)) AS shortest
FROM tmp;