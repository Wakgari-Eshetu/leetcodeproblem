SELECT 
  ROUND(
    COUNT(DISTINCT CASE WHEN DATEDIFF(a.event_date, f.first) = 1 THEN a.player_id END)
    / COUNT(DISTINCT f.player_id),
    2
  ) AS fraction
FROM Activity a
RIGHT JOIN (
    SELECT player_id, MIN(event_date) AS first
    FROM Activity
    GROUP BY player_id
) f
ON a.player_id = f.player_id;
