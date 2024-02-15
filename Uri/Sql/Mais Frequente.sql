SELECT
    amount AS most_frequent_value
FROM
    (
        SELECT
            amount,
            COUNT(amount) as frequent
        FROM
            value_table
        GROUP BY
            amount
        ORDER BY
            amount
    ) value_frequent
ORDER BY
    frequent DESC
LIMIT
    1

-- OUTRA OPÇÂO MAIS SIMPLES

SELECT amount AS most_frequent_value
FROM value_table
GROUP BY amount
ORDER BY COUNT(amount) DESC
LIMIT 1;
