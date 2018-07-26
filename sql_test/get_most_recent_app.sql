SELECT a.pk, a.id, a.title, a.rating, a.last_update_date FROM apps a join 
(SELECT id, MAX(last_update_date) from apps
GROUP BY id) as b on a.id = b.id and a.last_update_date = b.max;