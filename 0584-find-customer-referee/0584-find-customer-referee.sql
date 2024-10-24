# Write your MySQL query statement below
# names of customer that are do not have referee_id of 2
SELECT name 
FROM customer
WHERE referee_id != 2 or referee_id is NULL
