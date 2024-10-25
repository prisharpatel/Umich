# Write your MySQL query statement below
SELECT DISTINCT W.id 
FROM Weather W 
JOIN Weather W2 ON W.id != W2.id
WHERE W.recordDate > W2.recordDate AND DATEDIFF(W.recordDate, W2.recordDate) = 1 AND W.temperature > W2.temperature