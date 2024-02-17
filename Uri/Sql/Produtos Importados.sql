SELECT
    p.name,
    pr.name,
    c.name
FROM
    products p
    INNER JOIN providers pr ON p.id_providers = pr.id
    INNER JOIN categories c ON p.id_categories = c.id
WHERE
    pr.name = 'Sansul SA'
    AND c.name = 'Imported';