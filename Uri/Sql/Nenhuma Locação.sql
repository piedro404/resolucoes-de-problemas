SELECT c.id, c.name 
FROM customers c FULL JOIN locations l
ON c.id = l.id_customers
WHERE l.id IS NULL
ORDER BY c.id;