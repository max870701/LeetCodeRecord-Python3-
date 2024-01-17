SELECT survey_log
FROM (
    SELECT 
        s.question_id AS "survey_log", 
        SUM(CASE WHEN s.action = 'answer' THEN 1.0 ELSE 0 END) / NULLIF(SUM(CASE WHEN s.action = 'show' THEN 1.0 ELSE 0 END), 0) AS "answer_rate"
    FROM SurveyLog AS s
    WHERE s.action != 'skip'
    GROUP BY s.question_id
) AS rate_query
ORDER BY answer_rate DESC, survey_log
LIMIT 1;