# Write your MySQL query statement below
WITH CTE AS (
    SELECT product_id, MAX(CASE WHEN change_date <= '2019-08-16' THEN change_date END) AS change_date
    FROM Products
    GROUP BY product_id
)

SELECT C.product_id, COALESCE(P.new_price,10) AS price 
FROM CTE C
LEFT JOIN Products P using(product_id,change_date)
