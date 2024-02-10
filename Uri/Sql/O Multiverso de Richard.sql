-- Não Foi Aprovado, Porém Correto nos Testes

SELECT lr.name, ROUND(lr.omega * 1.618, 3) AS "Fator N"
FROM life_registry lr INNER JOIN dimensions d 
ON d.id = lr.dimensions_id
WHERE (d.name = 'C774' 
OR d.name = 'C875')
AND lr.name LIKE "Richard%"
ORDER BY lr.omega;

