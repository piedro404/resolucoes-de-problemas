SELECT
    CASE
        WHEN u_1.posts < u_2.posts THEN u_1.user_name
        ELSE u_2.user_name
    END AS u1_name,
    CASE
        WHEN u_2.posts > u_1.posts THEN u_2.user_name
        ELSE u_1.user_name
    END AS u2_name
FROM
    users u_1
    INNER JOIN followers f ON u_1.user_id = f.user_id_fk
    INNER JOIN users u_2 ON f.following_user_id_fk = u_2.user_id
WHERE
    u_1.user_id < f.following_user_id_fk
    AND EXISTS (
        SELECT
            1
        FROM
            followers AS f2
        WHERE
            f2.user_id_fk = u_2.user_id
            AND f2.following_user_id_fk = u_1.user_id
    )
ORDER BY
    CASE
        WHEN u_1.posts < u_2.posts THEN u_1.user_id
        ELSE u_2.user_id
    END