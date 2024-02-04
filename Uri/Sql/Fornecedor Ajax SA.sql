select p.name, pr.name
from products p inner join providers pr
on p.id_providers=pr.id
where pr.name = 'Ajax SA';