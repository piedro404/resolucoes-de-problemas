(
    SELECT
        name
    FROM
        (
            SELECT
                CONCAT('Podium: ', team) AS name,
                position
            FROM
                league
            ORDER BY
                position
            LIMIT
                3
        ) AS top_teams
    ORDER BY
        position
)
UNION
ALL (
    SELECT
        name
    FROM
        (
            SELECT
                CONCAT('Demoted: ', team) AS name,
                position
            FROM
                league
            ORDER BY
                position DESC
            LIMIT
                2
        ) AS bottom_teams
    ORDER BY
        position
)