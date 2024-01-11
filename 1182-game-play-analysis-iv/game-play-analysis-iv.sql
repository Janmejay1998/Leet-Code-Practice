# Write your MySQL query statement below
WITH T AS (
    SELECT player_id, DATEDIFF(event_date, MIN(event_date) OVER (PARTITION BY player_id)) = 1 AS player_login 
    FROM Activity
)

SELECT ROUND(SUM(player_login)/COUNT(DISTINCT player_id),2) AS fraction
FROM T