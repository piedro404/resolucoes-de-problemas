SELECT
    queue,
    adjacent.left,
    adjacent.right
FROM
    (
        SELECT
            queue,
            id AS "left",
            LEAD(id) OVER (
                PARTITION BY queue
                ORDER BY
                    id
            ) AS "right"
        FROM
            chairs
        WHERE
            available = TRUE
) adjacent
WHERE
    adjacent.left+1 = adjacent.right
ORDER BY
    queue,
    adjacent.left