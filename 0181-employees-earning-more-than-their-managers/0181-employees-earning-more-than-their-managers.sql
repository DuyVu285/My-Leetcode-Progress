# Write your MySQL query statement below
SELECT worker.name AS Employee FROM Employee AS worker
WHERE worker.salary > (SELECT manager.salary FROM Employee AS manager WHERE manager.id = worker.managerId)