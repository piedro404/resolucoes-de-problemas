select c.name, r.rentals_date
from customers c inner join rentals r 
on r.id_customers = c.id
where EXTRACT('month' from r.rentals_date) = 9;