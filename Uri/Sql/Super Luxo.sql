select p.name, pr.name, p.price
from products p inner join providers pr 
on pr.id = p.id_providers 
inner join categories c
on c.id = p.id_categories
where p.price>1000 and c.name='Super Luxury';