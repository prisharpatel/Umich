# Write your MySQL query statement below
# number of times a customer visited without making transactions 
# group visits together by customer id if visit id doesn't equal something in transactions 
# count that group to include int able
SELECT V.customer_id, COUNT(V.customer_id) AS count_no_trans
FROM Visits V
WHERE V.visit_id NOT IN (SELECT T.visit_id FROM Transactions T)
GROUP BY V.customer_id