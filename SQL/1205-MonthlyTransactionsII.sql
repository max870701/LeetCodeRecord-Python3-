WITH table1 AS (
    SELECT
        TO_CHAR(trans_date, 'YYYY-MM') AS month,
        country,
        COUNT(amount) AS approved_count,
        SUM(amount) AS approved_amount,
        0 AS chargeback_count,
        0 AS chargeback_amount
    FROM Transactions
    WHERE state = 'approved'
    GROUP BY month, country
    UNION
    SELECT
        TO_CHAR(c.trans_date, 'YYYY-MM') AS month,
        t.country,
        0 AS approved_count,
        0 AS approved_amount,
        COUNT(c.trans_id) AS chargeback_count,
        SUM(t.amount) AS chargeback_amount
    FROM Chargebacks AS c
    LEFT JOIN Transactions AS t
    ON t.id = c.trans_id
    GROUP BY month, country
)

SELECT
    month,
    country,
    SUM(approved_count) AS approved_count,
    SUM(approved_amount) AS approved_amount,
    SUM(chargeback_count) AS chargeback_count,
    SUM(chargeback_amount) AS chargeback_amount
FROM table1
GROUP BY month, country