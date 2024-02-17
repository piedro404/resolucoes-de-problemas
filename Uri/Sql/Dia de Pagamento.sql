SELECT
    name,
    CAST(
        EXTRACT(
            'day'
            FROM
                payday
        ) AS INTEGER
    ) AS day
FROM
    loan;