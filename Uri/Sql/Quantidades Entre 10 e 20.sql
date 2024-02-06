select p.name 
from providers pr inner join products p
on p.id_providers = pr.id
where p.amount >10 and p.amount<20  and pr.name like 'P%';