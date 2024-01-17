SELECT a.actor_id, a.director_id
FROM ActorDirector AS a
GROUP BY a.actor_id, a.director_id
HAVING COUNT(a.director_id) >= 3;