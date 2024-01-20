WITH s_grade AS (
    SELECT student_id, MAX(grade)
    FROM Enrollments
    GROUP BY student_id
)

SELECT student_id, MIN(course_id) AS "course_id", grade
FROM Enrollments
WHERE (student_id, grade) IN (SELECT * FROM s_grade)
GROUP BY student_id, grade
ORDER BY student_id;