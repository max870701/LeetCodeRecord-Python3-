SELECT sub.class
FROM 
(
    SELECT c.class, COUNT(c.student) AS "student_number"
    FROM Courses AS c
    GROUP BY c.class
    ORDER BY "student_number" DESC
) AS sub
WHERE sub.student_number >= 5;