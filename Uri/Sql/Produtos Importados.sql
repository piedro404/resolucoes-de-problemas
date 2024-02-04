select p.name, pr.name, c.name
from products p inner join providers pr
on p.id_providers = pr.id 
inner join categories c
on p.id_categories = c.id
where pr.name = 'Sansul SA' and c.name = 'Imported';