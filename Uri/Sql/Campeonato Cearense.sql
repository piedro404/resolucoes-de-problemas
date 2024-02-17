SELECT
	t.name,
	COUNT(m.id) AS matches,
	SUM(
		CASE
			WHEN m.team_1 = t.id
			AND m.team_1_goals > m.team_2_goals THEN 1
			WHEN m.team_2 = t.id
			AND m.team_2_goals > m.team_1_goals THEN 1
			ELSE 0
		END
	) AS victories,
	SUM(
		CASE
			WHEN m.team_1 = t.id
			AND m.team_1_goals < m.team_2_goals THEN 1
			WHEN m.team_2 = t.id
			AND m.team_2_goals < m.team_1_goals THEN 1
			ELSE 0
		END
	) AS defeats,
	SUM(
		CASE
			WHEN m.team_1 = t.id
			AND m.team_1_goals = m.team_2_goals THEN 1
			WHEN m.team_2 = t.id
			AND m.team_2_goals = m.team_1_goals THEN 1
			ELSE 0
		END
	) AS draws,
	(
		SUM(
			CASE
				WHEN m.team_1 = t.id
				AND m.team_1_goals > m.team_2_goals THEN 3
				WHEN m.team_2 = t.id
				AND m.team_2_goals > m.team_1_goals THEN 3
				WHEN m.team_1 = t.id
				AND m.team_1_goals = m.team_2_goals THEN 1
				WHEN m.team_2 = t.id
				AND m.team_2_goals = m.team_1_goals THEN 1
				ELSE 0
			END
		)
	) AS score
FROM
	teams t
	LEFT JOIN matches m ON m.team_1 = t.id
	OR m.team_2 = t.id
GROUP BY
	t.id
ORDER BY
	score DESC,
	victories DESC,
	draws DESC,
	defeats -- Modo Otimizado mais não aceito na URI, teste realizado na DB
SELECT
	name,
	matches,
	victories,
	defeats,
	draws,
	((victories * 3) +(draws)) AS score
FROM
	(
		SELECT
			t.name AS name,
			COUNT(m.id) AS matches,
			SUM(
				CASE
					WHEN m.team_1 = t.id
					AND m.team_1_goals > m.team_2_goals THEN 1
					WHEN m.team_2 = t.id
					AND m.team_2_goals > m.team_1_goals THEN 1
					ELSE 0
				END
			) AS victories,
			SUM(
				CASE
					WHEN m.team_1 = t.id
					AND m.team_1_goals < m.team_2_goals THEN 1
					WHEN m.team_2 = t.id
					AND m.team_2_goals < m.team_1_goals THEN 1
					ELSE 0
				END
			) AS defeats,
			SUM(
				CASE
					WHEN m.team_1 = t.id
					AND m.team_1_goals = m.team_2_goals THEN 1
					WHEN m.team_2 = t.id
					AND m.team_2_goals = m.team_1_goals THEN 1
					ELSE 0
				END
			) AS draws
		FROM
			teams t
			LEFT JOIN matches m ON m.team_1 = t.id
			OR m.team_2 = t.id
		GROUP BY
			t.id
	)
ORDER BY
	score DESC,
	victories DESC,
	draws DESC,
	defeats