select p.name, c.name 
from providers c inner join products p on p.id_providers=c.id 
inner join categories cl on p.id_categories=cl.id
where cl.id = 6;