
-- JOINS
-- 1. Find the total salary expenditure for each department.
SELECT d.Name AS DepartmentName, SUM(e.Salary) AS TotalSalaryExpenditure
FROM EMPLOYEE e
JOIN Department d ON e.DepartmentID = d.ID
Group BY d.Name;

-- 2.Query to find the average salary of employees in each department.
SELECT d.Name AS DepartmentName, AVG(e.Salary) AS AverageSalary
FROM Employee e
JOIN Department d ON e.DepartmentID = d.ID
GROUP BY d.Name;

-- 3. Query to get the list of employees who are in the same department as 'John'.
SELECT e.Name
FROM Employee e
WHERE e.DepartmentID = (
    SELECT DepartmentID
    FROM Employee
    WHERE Name = 'JOhn'
);

-- 4. Query to find employees who do not belong to the 'IT' department (must use join)
SELECT e.Name, e.DepartmentID
FROM Employee e
JOIN Department d ON e.DepartmentID = d.ID
WHERE d.Name <> 'IT';

-- 5. Query to find the department with highest salary expenditure.
SELECT TOP 1 d.Name AS DepartmentName, SUM(e.Salary) AS TotalSalaryExpenditure
FROM Employee e
JOIN Department d ON e.DepartmentID = d.ID
GROUP BY d.Name
ORDER BY TotalSalaryExpenditure DESC;

-- 6. Query to get the names of employees who have the same salary as the maximum
--  salary in the 'HR' department.
SELECT e.Name
FROM Employee e
JOIN (
    SELECT MAX(Salary) AS MaxSalary
    FROM Employee 
    WHERE DepartmentID = (SELECT  ID FROM DEPARTMENT WHERE Name = 'HR')
    ) AS MaxSalaryHR ON e.Salary = MaxSalaryHR.MaxSalary
    WHERE e.DepartmentID = (SELECT ID FROM Department WHERE Name = 'HR');

-- Randomly
SELECT MAX(Salary) AS MaxSalary
FROM Employee
WHERE DepartmentID = (SELECT ID FROM Department WHERE Name = 'HR');

-- 7. Query to list all employees and their departments, displaying 
-- 'No Department' for employees without a department.

SELECT e.Name AS EmployeeName,
ISNULL(d.Name, 'No Department') AS DepartmentName
FROM Employee e
LEFT JOIN Department d ON e.DepartmentID = d.ID;

-- 8. Query to find departments that have employees with salaries 
-- above the average salary of all employees
SELECT d.Name AS DepartmentName
FROM Department d
JOIN (
    SELECT AVG(Salary) AS AvgSalary
    FROM Employee
) AS AvgSal ON 1=1
JOIN Employee e ON d.ID = e.DepartmentID
WHERE e.Salary > AvgSal.AvgSalary;

-- 9. Query to find the departments that have more than one employee with the same salary.
SELECT d.Name AS DepartmentName
FROM Department d
JOIN Employee e ON d.ID = e.DepartmentID
GROUP BY d.ID, d.Name, e.Salary
HAVING COUNT(*) > 1;
