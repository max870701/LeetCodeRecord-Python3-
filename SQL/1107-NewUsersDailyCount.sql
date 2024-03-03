-- Solution 1
WITH first_login AS (
    SELECT
        user_id,
        MIN(activity_date) AS login_date
    FROM Traffic
    WHERE activity = 'login'
    GROUP BY 1
)

SELECT
    login_date,
    COUNT(user_id) AS user_count
FROM first_login
WHERE login_date BETWEEN ('2019-06-30'::DATE - INTERVAL '90 days')
AND '2019-06-30'::DATE
GROUP BY 1

-- Solution 2
WITH first_login AS (
  SELECT 
    user_id, 
    activity_date AS login_date,
    ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY activity_date) AS rn
  FROM Traffic
  WHERE activity = 'login'
)

SELECT 
  login_date, 
  COUNT(user_id) AS user_count
FROM first_login
WHERE rn = 1
AND login_date BETWEEN ('2019-06-30'::DATE - INTERVAL '90 days') AND '2019-06-30'::DATE
GROUP BY login_date