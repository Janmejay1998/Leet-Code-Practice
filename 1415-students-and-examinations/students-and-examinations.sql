# Write your MySQL query statement below
WITH SS AS (                         # Using Common Table Expression (CTE) method
    SELECT *                         # Joining Student and Subjects
    FROM Students
    JOIN Subjects
)

 # Joining SS and Examinations
SELECT SS.student_id, SS.student_name, SS.subject_name, COUNT(E.subject_name) AS attended_exams
FROM SS
LEFT JOIN Examinations E ON SS.student_id = E.student_id 
AND SS.subject_name = E.subject_name
GROUP BY student_id, subject_name
ORDER BY student_id, subject_name;
