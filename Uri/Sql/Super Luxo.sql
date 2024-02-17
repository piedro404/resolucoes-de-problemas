SELECT
    p.name,
    pr.name,
    p.price
FROM
    products p
    INNER JOIN providers pr ON pr.id = p.id_providers
    INNER JOIN categories c ON c.id = p.id_categories
WHERE
    p.price > 1000
    AND c.name = 'Super Luxury';