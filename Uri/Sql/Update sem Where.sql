SELECT
    name,
    price
FROM
    (
        SELECT
            id,
            name,
            CASE
                WHEN type = 'A' THEN 20.0
                WHEN type = 'B' THEN 70.0
                ELSE 530.5
            END AS price
        FROM
            products
    ) new_products
ORDER BY
    price,
    id DESC