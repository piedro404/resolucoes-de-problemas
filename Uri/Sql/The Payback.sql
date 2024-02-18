SELECT
    c.name,
    c.investment,
    MIN(o.month) AS month_of_payback,
    MIN(saldo_acumulado)-c.investment AS "return"
FROM
    clients c
    INNER JOIN (
        SELECT
            client_id,
            month,
            SUM(profit) OVER (
                PARTITION BY client_id
                ORDER BY
                    month
            ) AS saldo_acumulado
        FROM
            operations
    ) o ON c.id = o.client_id
WHERE
    o.saldo_acumulado >= c.investment
GROUP BY
    o.client_id,
    c.name,
    c.investment
ORDER BY
    MIN(saldo_acumulado)-c.investment DESC