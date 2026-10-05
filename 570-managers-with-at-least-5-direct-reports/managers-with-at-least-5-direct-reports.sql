/* Write your T-SQL query statement below */
SELECT e.name
FROM Employee e
JOIN Employee m
ON e.id=m.managerID
GROUP BY m.managerID,e.name
HAVING COUNT(m.managerID)>=5;