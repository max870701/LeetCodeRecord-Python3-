WITH customer_contacts AS (
    SELECT
        c1.customer_id,
        c1.customer_name,
        c2.contact_name
    FROM Customers AS c1
    LEFT JOIN Contacts AS c2
    ON c1.customer_id = c2.user_id
), contact_stats AS (
    SELECT
        c1.customer_id,
        c1.customer_name,
        COUNT(c1.contact_name) AS contacts_cnt,
        COUNT(c2.customer_id) AS trusted_contacts_cnt
    FROM customer_contacts AS c1
    LEFT JOIN Customers AS c2
    ON c1.contact_name = c2.customer_name
    GROUP BY 
        c1.customer_id,
        c1.customer_name
)

SELECT
    i.invoice_id,
    c.customer_name,
    i.price,
    c.contacts_cnt,
    c.trusted_contacts_cnt
FROM Invoices AS i
INNER JOIN contact_stats AS c
ON i.user_id = c.customer_id
ORDER BY i.invoice_id;