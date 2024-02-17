SELECT
    d.name,
    ROUND(salario, 1) AS salary
FROM
    doctors d
    LEFT JOIN (
        SELECT
            att.id_doctor,
            SUM(
                (att.hours * 150) +((att.hours * 150) *(ws.bonus / 100))
            ) AS salario
        FROM
            attendances att
            LEFT JOIN work_shifts ws ON att.id_work_shift = ws.id
        GROUP BY
            att.id_doctor
    ) salario ON d.id = salario.id_doctor
ORDER BY
    salary DESC