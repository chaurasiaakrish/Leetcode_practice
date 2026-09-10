/* Write your T-SQL query statement below */
SELECT Activity.machine_id, ROUND(AVG(A1.timestamp-Activity.timestamp),3) AS processing_time
FROM Activity
JOIN Activity AS A1
ON Activity.machine_id=A1.machine_id AND Activity.process_id=A1.process_id
WHERE Activity.activity_type='start' AND A1.activity_type='end'
GROUP BY Activity.machine_id