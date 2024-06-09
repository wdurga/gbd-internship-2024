-- SQL SERVER DAY-1

-- 1. Create table Employee and Department with Department Id of 
-- Employee foreign key to table Department.

-- create department table::
CREATE TABLE DEPARTMENT (
    ID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL
);

-- insert data into department table::
INSERT INTO DEPARTMENT (ID, Name) VALUES
(1, 'IT'),
(2, 'Admin'),
(3, 'HR'),
(4, 'Accounts'),
(5, 'Health');

SELECT * FROM DEPARTMENT;

-- Create employee table::
CREATE TABLE EMPLOYEE (
    ID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    DEPARTMENTID INT,
    Salary INT,
    Active BIT,
    FOREIGN KEY (DEPARTMENTID) REFERENCES DEPARTMENT(ID)
);
-- insert data into employee table::
INSERT INTO EMPLOYEE (ID, Name, DEPARTMENTID, Salary, Active) VALUES
(1, 'John', 1, 2000, 1),
(2, 'Sean', 1, 4000, 1),
(3, 'Eric', 2, 2000, 1),
(4, 'Nancy', 2, 2000, 1),
(5, 'Lee', 3, 3000, 1),
(6, 'Steven', 4, 2000, 1),
(7, 'Matt', 1, 5000, 1),
(8, 'Sarah', 1, 2000, 0);

SELECT * FROM EMPLOYEE;
DROP TABLE EMPLOYEE;
DROP TABLE DEPARTMENT;

-- 2. Write a query to get employee list in ascending order of their salary.
SELECT * 
FROM EMPLOYEE
ORDER BY Salary ASC;

-- 3. Write a query to get distinct salary from Employee table.
SELECT DISTINCT Salary
FROM EMPLOYEE;

-- 4. Write a query to find total number of active employees.
SELECT COUNT(*)
FROM EMPLOYEE
WHERE Active = 1;

-- count total no. of active employees with column name as ActiveEmployeeCount
SELECT COUNT(*) AS ActiveEmployeeCount
FROM EMPLOYEE
WHERE Active = 1;

-- 5. Update the Department of Nancy to HR.
UPDATE EMPLOYEE
SET DEPARTMENTID =(SELECT ID FROM DEPARTMENT WHERE Name ='HR')
WHERE Name = 'Nancy';

-- 6. Write a query to get a record of employee with highest and second highest salary.
SELECT TOP 1 *
FROM Employee
ORDER BY Salary DESC;

SELECT TOP 1 *
FROM (
SELECT TOP 2 *
FROM Employee
ORDER BY Salary DESC
) AS Temp
ORDER BY Salary ASC;

-- 7. Write a query to get department name of each employee.
SELECT E.ID, E.Name, E.Salary, E.Active, D.Name AS DepartmentName
FROM EMPLOYEE E
JOIN DEPARTMENT D
ON E.DEPARTMENTID = D.ID;

-- 8. Write a query to get department name with maximum employee count.
SELECT TOP 1
    D.Name AS DepartmentName,
    COUNT(E.ID) AS EmployeeCount
FROM
    Department D
JOIN
    Employee E ON D.ID = E.DEPARTMENTID
GROUP BY
    D.Name
ORDER BY
    COUNT(E.ID) DESC;

-- 9. Write a query to get departments where no Employee is assigned.
SELECT D.*
FROM DEPARTMENT D
LEFT JOIN EMPLOYEE E ON D.ID = E.DEPARTMENTID
WHERE E.ID IS NULL;

-- 10.Write a query to get list of employee and salary with same salary.
SELECT Name, Salary
FROM EMPLOYEE
WHERE Salary IN (
    SELECT Salary
    FROM EMPLOYEE
    GROUP BY Salary
    HAVING COUNT(*) > 1
)
ORDER BY Salary;