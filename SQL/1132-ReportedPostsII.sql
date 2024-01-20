WITH reported_posts AS (
    SELECT action_date, extra, post_id
    FROM Actions
    WHERE extra = 'spam'
    GROUP BY action_date, extra, post_id
), dp AS (
    SELECT r1.action_date, (COUNT(r2.post_id)::FLOAT / COUNT(r1.post_id)) AS "daily_percent"
    FROM reported_posts AS r1
    LEFT JOIN Removals AS r2
    ON r1.post_id = r2.post_id
    GROUP BY r1.action_date
)

SELECT ROUND(AVG(daily_percent)::NUMERIC * 100, 2)
AS "average_daily_percent"
FROM dp;