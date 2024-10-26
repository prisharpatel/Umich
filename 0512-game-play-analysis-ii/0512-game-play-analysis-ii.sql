# Write your MySQL query statement below

-- report the device that is first logged in for each player 

-- group by player
-- choose the earliest event date from each group and select device that matches that one 
WITH min_data AS ( 
    SELECT MIN(event_date) AS event_date, A1.player_id
    FROM Activity A1
    GROUP BY A1.player_id
)
SELECT A.player_id, A.device_Id
FROM Activity A, min_data M
WHERE M.player_id = A.player_id 
AND A.event_date = M.event_date
