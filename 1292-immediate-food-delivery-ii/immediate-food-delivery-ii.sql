# Write your MySQL query statement below
WITH S1 AS (SELECT customer_id, Min(order_date) AS order_date
FROM Delivery
GROUP BY customer_id)

SELECT ROUND(100*AVG(order_date = customer_pref_delivery_date),2) AS immediate_percentage
FROM Delivery
JOIN S1 USING(customer_id,order_date);