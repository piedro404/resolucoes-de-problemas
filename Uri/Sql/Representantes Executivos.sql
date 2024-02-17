SELECT
    p.name,
    c.name
FROM
    providers c
    INNER JOIN products p ON p.id_providers = c.id
    INNER JOIN categories cl ON p.id_categories = cl.id
WHERE
    cl.id = 6;