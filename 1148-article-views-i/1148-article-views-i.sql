# Write your MySQL query statement below
# no primary key - duplicate rows (USE DISTINCT)
# find all authors 
# where they viewed at least one of their own articles 
# sort by id in ASC

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id ASC;