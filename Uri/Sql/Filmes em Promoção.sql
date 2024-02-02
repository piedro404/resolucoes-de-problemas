select m.id, m.name
from movies m inner join prices p
on p.id = m.id_prices
where p.value < 2.00