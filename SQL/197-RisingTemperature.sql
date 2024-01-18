-- SELECT w1.id, w1.recordDate, w1.temperature AS "current_temp", w2.recordDate , w2.temperature AS "previous_temp"
SELECT w1.id
FROM Weather AS w1
LEFT JOIN Weather AS w2
ON w1.recordDate = w2.recordDate + INTERVAL '1 day'
WHERE w1.temperature > w2.temperature;