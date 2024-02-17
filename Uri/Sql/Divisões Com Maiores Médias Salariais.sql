SELECT
    departamento,
    divisao,
    media
FROM
    (
        SELECT
            d.nome AS departamento,
            dv.nome AS divisao,
            ROUND(AVG(salario_liquido), 2) AS media,
            ROW_NUMBER() OVER (
                PARTITION BY d.nome
                ORDER BY
                    ROUND(AVG(salario_liquido), 2) DESC
            ) AS ranking
        FROM
            departamento d
            INNER JOIN divisao dv ON d.cod_dep = dv.cod_dep
            LEFT JOIN empregado e ON dv.cod_divisao = e.lotacao_div
            LEFT JOIN (
                SELECT
                    salario_bruto.matr AS matr,
                    COALESCE(salario_bruto.valor, 0) AS salario_bruto,
                    COALESCE(descontos.total_desconto, 0) AS descontos,
                    (
                        COALESCE(salario_bruto.valor, 0) - COALESCE(descontos.total_desconto, 0)
                    ) AS salario_liquido
                FROM
                    (
                        SELECT
                            e.matr,
                            SUM(COALESCE(v.valor, 0)) AS valor
                        FROM
                            empregado e
                            LEFT JOIN emp_venc ev ON e.matr = ev.matr
                            LEFT JOIN vencimento v ON ev.cod_venc = v.cod_venc
                        GROUP BY
                            e.matr
                    ) salario_bruto
                    LEFT JOIN (
                        SELECT
                            e.matr,
                            SUM(COALESCE(valor, 0)) AS total_desconto
                        FROM
                            empregado e
                            LEFT JOIN emp_desc ed ON e.matr = ed.matr
                            LEFT JOIN desconto de ON ed.cod_desc = de.cod_desc
                        GROUP BY
                            e.matr
                    ) descontos ON salario_bruto.matr = descontos.matr
            ) salario ON e.matr = salario.matr
        GROUP BY
            d.nome,
            dv.nome
        ORDER BY
            media DESC
    ) ranking_departamentos
WHERE
    ranking = 1
ORDER BY
    media DESC