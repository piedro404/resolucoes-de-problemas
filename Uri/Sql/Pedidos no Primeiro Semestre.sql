SELECT
    c.name,
    o.id
FROM
    customers c
    INNER JOIN orders o ON o.id_customers = c.id
WHERE
    EXTRACT(
        'month'
        FROM
            o.orders_date
    ) <= 6;