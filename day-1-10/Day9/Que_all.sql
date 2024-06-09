
-- SQL__DAY 3
-- 1. Write a query to find the employees who have the highest 
-- salary in their respective departments. Use INNER JOIN to get the department names.

SELECT e1.ID, e1.Name, e1.Salary, e1.Active, d.Name AS DepartmentName
FROM Employee e1
INNER JOIN Department d ON e1.departmentiD = d.ID
WHERE e1.Salary = (
    SELECT MAX(e.Salary)
    FROM Employee e
    WHERE e.departmentID = e1.departmentID
);

-- 
-- 2. Write a query to list all employees and their department names, but include
--  employees who do not belong to any department. Additionally, 
--  indicate if the employee is active or not.

SELECT e.ID, e.Name, E.Salary, e.Active, d.Name AS DepartmentName,
    CASE
        WHEN e.Active = 1 THEN 'Active'
        ELSE 'Inactive'
    END AS EmployeeeStatus
FROM Employee e
LEFT JOIN Department d ON e.departmentID = d.ID;

-- 3. Write a query to list all departments and the names of employees
--  who work in them. Include departments that do not have any employees assigned.

SELECT d.Name AS DepartmentName, e.Name AS EmployeeName
FROM Department d
LEFT JOIN Employee e ON d.Id = e.departmentID
ORDER BY d.name, e.Name;

-- 4. Write a query to list all employees and departments, including 
-- employees without departments and departments without employees. 

SELECT 
    e.ID AS EmployeeID, 
    e.Name AS EmployeeName,
    e.Salary AS EmployeeSalary, 
    e.Active AS EmployeeActive, 
    d.ID AS DepartmentID,
    d.Name AS DepartmentName
FROM Employee e
FULL OUTER JOIN Department d ON e.departmentID = d.Id;

-- 5. Write a query to find the total salary expenditure and the average
--  salary for each department, including departments without any employees.

SELECT 
d.ID AS DepartmentID, 
d.Name AS DepartmentName,
SUM(e.Salary) AS TotalSalaryExpenditure,
AVG(e.Salary) AS AverageSalary
FROM Department d
LEFT JOIN Employee e ON d.ID = e.DepartmentID
GROUP BY d.ID, d.Name;


--  6. Write a query using a CTE to list the employees who have a salary above
--  the average salary of their department. Include the department name in the results.

WITH DepartmentAvgSalary AS (
    SELECT e.departmentID, AVG(e.Salary) AS AvgSalary
    FROM Employee e
    GROUP BY e.departmentID
)
SELECT
    e.Name AS EmployeeName,
    e.Salary AS EmployeeSalary,
    d.Name AS DepartmentName
FROM Employee e
JOIN Department d ON e.departmentID = d.ID
JOIN DepartmentAvgSalary das AS e.DepartmentID = das.DepartmentID
WHERE e.Salary > das.AvgSalary;

-- 7. Write a query to find the names of employees who earn more than the average
--  salary of all employees in the company. Include their department names.

SELECT e.Name AS EmployeeName, e.Salary AS EmployeeSalary, d.Name AS DepartmentName
FROM Employee e
JOIN department d ON e.departmentID = d.ID
WHERE e.Salary > (
    SELECT AVG(Salary)
    FROM Employee
);

-- 8. Write a query to list the names of employees who work in the same
--department as 'Sean' but exclude 'Sean' from the results.
--Use a CTE and INNER JOIN in your solution.

WITH SeanDepartment AS (
    SELECT DepartmentID
    FROM Employee
    WHERE Name ='Sean'
)
SELECT e.Name AS EmployeeName
FROM Employee e
JOIN SeanDepartment sd ON e.DepartmentID = sd.DepartmentID
WHERE e.Name != 'Sean';


-- 9. Write a query to find the department names which have more than one
--  employee earning above the average salary of their department.
--   Use nested subqueries and GROUP BY.

SELECT d.Name AS DepartmentName
FROM Department d
JOIN 
    (
        SELECT e.departmentID, COUNT(*) AS AboveAverageCount
        FROM Employee e
        WHERE e.Salary > (
            SELECT AVG(Salary)
            FROM Employee
            WHERE DepartmentID = e.DepartmentID
        )
        GROUP BY e.DepartmentID
    ) AS AboveAverage ON d.ID = AboveAverage.departmentID
    WHERE AboveAverageCount > 1;

-- 10. Write a query to find pairs of employees who work in the same department
--  and have the same salary. List each pair only once.
SELECT 
    e1.Name AS Employee1,
    e2.Name AS Employee2,
    d.Name AS Department,
    e1.Salary AS Salary
FROM Employee e1
JOIN Employee e2 ON e1.departmentID = e2.DepartmentID AND e1.Salary = e2.Salary AND e1.ID < e2.ID
JOIN Department d ON e1.DepartmentID = d.ID;
