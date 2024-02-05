select c.name, o.id
from customers c inner join orders o
on o.id_customers = c.id
where EXTRACT('month' from o.orders_date) <= 6;