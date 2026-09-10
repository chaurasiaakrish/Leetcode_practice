/* Write your T-SQL query statement below */
SELECT Employee.name,Bonus.bonus
FROM Employee
LEFT JOIN BONUS
ON Employee.empID=Bonus.empID
WHERE Bonus.bonus < 1000 or Bonus.bonus IS NULL