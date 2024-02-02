select m.id, m.name
from movies m inner join genres g
on m.id_genres = g.id
where g.description = 'Action'