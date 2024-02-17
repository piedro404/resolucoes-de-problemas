WITH max_customers AS (
    SELECT
        name,
        customers_number
    FROM
        lawyers
    ORDER BY
        customers_number DESC
    LIMIT
        1
), min_customers AS (
    SELECT
        name,
        customers_number
    FROM
        lawyers
    ORDER BY
        customers_number ASC
    LIMIT
        1
), average_customers AS (
    SELECT
        'Average' AS name,
        ROUND(AVG(customers_number)) AS customers_number
    FROM
        lawyers
)
SELECT
    *
FROM
    max_customers
UNION
ALL
SELECT
    *
FROM
    min_customers
UNION
ALL
SELECT
    *
FROM
    average_customers;