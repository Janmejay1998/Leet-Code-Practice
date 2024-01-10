# Write your MySQL query statement below
SELECT EM.unique_id, E.name
FROM Employees E
LEFT JOIN EmployeeUNI EM ON E.id = EM.id;