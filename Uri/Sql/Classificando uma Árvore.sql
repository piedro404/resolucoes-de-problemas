SELECT
    DISTINCT n.node_id,
    COALESCE(
        CASE
            WHEN n.pointer IS NULL THEN 'LEAF'
            WHEN p.node_id IS NULL THEN 'ROOT'
            ELSE 'INNER'
        END,
        'LEAF'
    ) AS type
FROM
    nodes n
LEFT JOIN
    nodes p ON n.node_id = p.pointer
ORDER BY
    node_id;
