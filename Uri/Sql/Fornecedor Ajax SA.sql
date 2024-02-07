SELECT p.name, pr.name
FROM products p INNER JOIN providers pr
ON p.id_providers=pr.id
WHERE pr.name = 'Ajax SA';