# Write your MySQL query statement below
# find id's of tweets
# WHERE number of characters used in th econtent of the tweet is > 15 
SELECT tweet_id 
FROM Tweets
WHERE CHAR_LENGTH(content) > 15
