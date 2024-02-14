SELECT
    e.cpf,
    e.enome,
    d.dnome
FROM
    empregados e
    INNER JOIN departamentos d ON e.dnumero = d.dnumero
    LEFT JOIN trabalha t ON e.cpf = t.cpf_emp
WHERE
    t.cpf_emp IS NULL
ORDER BY
    e.cpf