SELECT p.name 
FROM providers pr INNER JOIN products p
ON p.id_providers = pr.id
WHERE p.amount > 10 
AND p.amount< 20 
AND pr.name LIKE 'P%';