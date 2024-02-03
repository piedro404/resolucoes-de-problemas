select c.id, c.name 
from customers c full join locations l
on c.id = l.id_customers
where l.id is NULL
order by c.id;