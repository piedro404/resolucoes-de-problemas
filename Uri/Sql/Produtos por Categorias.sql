select c.name,sum(p.amount) as sum
from products p inner join categories c
on p.id_categories = c.id 
group by c.name;
