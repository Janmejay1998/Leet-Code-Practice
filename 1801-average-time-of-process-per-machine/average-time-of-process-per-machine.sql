# Write your MySQL query statement below
SELECT A1.machine_id, 
ROUND(AVG(A1.timestamp - A2.timestamp),3) AS processing_time    # Rounding of upto 3 decimal places
FROM Activity A1
JOIN Activity A2 ON A1.machine_id = A2.machine_id         # Self Joining
AND A1.process_id = A2.process_id                         # Linking on process_id
AND A1.timestamp > A2.timestamp                           # For the logic of end timestamp > start timestamp
GROUP BY A1.machine_id;                                   # Grouping on machine_id of A1 table
