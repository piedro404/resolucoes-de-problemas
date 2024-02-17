SELECT
    p.year,
    sender.name,
    receiver.name
FROM
    packages p
    INNER JOIN users sender ON p.id_user_sender = sender.id
    INNER JOIN users receiver ON p.id_user_receiver = receiver.id
WHERE
    (
        p.color = 'blue'
        OR p.year = 2015
    )
    AND (
        sender.address != 'Taiwan'
        AND receiver.address != 'Taiwan'
    )
ORDER BY
    p.year DESC