# Write your MySQL query statement below
WITH CTE AS (
    SELECT person_name, SUM(weight) OVER (ORDER BY turn) AS total
    FROM Queue
)

SELECT person_name
FROM CTE
WHERE total <= 1000
ORDER BY total DESC
LIMIT 1