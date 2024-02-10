-- Não Foi Aprovado, Porém Correto nos Testes

SELECT CONCAT("Approved: ", name) AS name, ROUND(grade, 1) AS grade
FROM students
WHERE grade >= 7.0
ORDER BY grade DESC;
