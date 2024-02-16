SELECT
    temperature,
    number_of_records
FROM
    (
        SELECT
            mark,
            temperature,
            COUNT(temperature) AS number_of_records
        FROM
            records
        GROUP BY
            mark,
            temperature
    ) count_sensor
ORDER BY
    mark