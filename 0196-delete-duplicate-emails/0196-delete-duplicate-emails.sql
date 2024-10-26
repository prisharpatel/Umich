-- # Write your MySQL query statement below
-- DELETE p1 FROM Person p1, Person p2
-- WHERE p1.email = p2.email AND p1.Id > p2.Id
WITH min_ids AS (
    SELECT MIN(id) 
    FROM Person 
    GROUP BY email
)
DELETE FROM Person 
WHERE id NOT IN (SELECT * FROM min_ids);
