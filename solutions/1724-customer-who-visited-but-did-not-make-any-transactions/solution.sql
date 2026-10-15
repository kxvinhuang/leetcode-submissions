-- Write your PostgreSQL query statement below
SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits
LEFT JOIN Transactions AS t USING(visit_id)
WHERE transaction_id IS NULL
GROUP BY customer_id
