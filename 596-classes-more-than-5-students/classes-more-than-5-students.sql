# Write your MySQL query statement below
WITH CTE AS (
    SELECT class, COUNT(*) AS count
    FROM Courses
    GROUP BY class
)

SELECT class
FROM CTE
WHERE count >= 5;