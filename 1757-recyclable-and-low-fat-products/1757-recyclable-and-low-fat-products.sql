# Write your MySQL query statement below
# find the ids of products that are low fat and recyclable

SELECT product_id
FROM products
WHERE low_fats = "Y" and recyclable = "Y"