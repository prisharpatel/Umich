# Write your MySQL query statement below
-- cancellation rate = canceled requests with unbanned users / total number of requests with unbanned users
-- WHERE request_at BETWEEN "2013-10-01" and "2013-10-03" 

SELECT T.request_at AS Day, ROUND(SUM(T.status!="completed")/COUNT(*), 2)AS 'Cancellation Rate'
FROM Trips T, Users Client, Users Driver
WHERE request_at BETWEEN "2013-10-01" and "2013-10-03" AND T.client_id = Client.users_id AND T.driver_id = Driver.users_id
AND Client.banned != "Yes" AND Driver.banned != "Yes"
GROUP BY T.request_at
