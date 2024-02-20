(SELECT
    city_name,
    population
FROM
    (
        SELECT
            city_name,
            population
        FROM
            cities
        ORDER BY
            population DESC
        LIMIT
            2
    ) first_2
ORDER BY
    population
LIMIT 1)
UNION ALL
(SELECT
    city_name,
    population
FROM
    (
        SELECT
            city_name,
            population
        FROM
            cities
        ORDER BY
            population
        LIMIT
            2
    ) end_2
ORDER BY
    population DESC
LIMIT 1)