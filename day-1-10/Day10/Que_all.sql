-- SQL DAY-4
-- Create table salesman, customer, order and insert data into it.

CREATE TABLE salesman (
    salesman_ID INT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    City VARCHAR(100),
    Commission DECIMAL(5, 2) CHECK (Commission >= 0.00),
);

INSERT INTO salesman (salesman_ID, Name, City, Commission) VALUES 
(5001, 'James Hooq', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5003, 'Lausoin Hen', NULL, 0.12),
(5007, 'Paul Adam', 'Rome', 0.13);

SELECT * FROM salesman;

CREATE TABLE customer (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    city VARCHAR(100),
    grade INT,
    salesman_ID INT,
    FOREIGN KEY (salesman_ID) REFERENCES salesman(salesman_ID)
);

INSERT INTO customer (customer_id, customer_name, city, grade, salesman_id) VALUES
(3002, 'Nick Rimando', 'New York', 100, 5001),
(3005, 'Graham Zusi', 'California', 200, 5002),
(3001, 'Brad Guzan', 'London', NULL, NULL),
(3004, 'Fabian Johns', 'Paris', 300, 5006),
(3007, 'Brad Davis', 'New York', 200, 5001),
(3009, 'Geoff Camero', 'Berlin', 100, NULL),
(3008, 'Julian Green', 'London', 300, 5002),
(3003, 'Jozy Altitdor', 'Moncow', 200, 5007);

SELECT * FROM customer;

CREATE TABLE [order] (
    order_no INT PRIMARY KEY,
    purch_amt DECIMAL(10, 2) CHECK (purch_amt >= 0),
    order_date DATE,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
    salesman_id INT,
    FOREIGN KEY (salesman_id) REFERENCES salesman(salesman_ID)
);

INSERT INTO [order] (order_no, purch_amt, order_date, customer_id, salesman_id) VALUES
(70001, 150.5, '2016-10-05', 3005, 5002),
(70009, 270.65, '2016-09-10', 3001, NULL),
(70002, 65.26, '2016-10-05', 3002, 5001),
(70004, 110.5, '2016-08-17', 3009, NULL),
(70007, 948.5, '2016-09-10', 3005, 5002),
(70005, 2400.6, '2016-07-27', 3007, 5001),
(70008, 5760, '2016-09-10', 3002, 5001),
(70010, 1983.43, '2016-10-10', 3004, 5006),
(70003, 2480.4, '2016-10-10', 3009, NULL),
(70012, 250.45, '2016-06-27', 3008, 5002),
(70011, 75.29, '2016-08-17', 3003, 5007);

SELECT * FROM [order];

-- Que 1. Find the name and city of those customers and salesmen who lives in the same city.
SELECT 
    c.customer_name AS CustomerName,
    c.city AS CustomerCity,
    s.name AS SalesmanName,
    s.city AS SalesmanCIty
FROM customer c
JOIN salesman s ON c.city = s.city;

-- QUE. 2. Find the names of all customers along with the salesmen who works for them.
SELECT 
    c.customer_name AS CustomerName,
    c.city AS CustomerCity,
    s.name AS SalesmanName,
    s.city AS SalesmanCity
FROM customer c
JOIN salesman s ON c.salesman_ID = s.salesman_ID;

-- Que. 3. Display all those orders by the customers not located
--  in the same cities where their salesmen live.

SELECT 
    o.order_no,
    o.purch_amt, 
    o.order_date,
    c.customer_name AS CustomerName,
    c.city AS CustomerCity, 
    s.name AS SalesmanName,
    s.city AS SalesmanCity
FROM [order] o
JOIN customer c ON o.customer_id = c.customer_id
JOIN salesman s ON o.salesman_id = s.salesman_ID 
WHERE c.city <> s.city;

-- Que. 4. Display all the orders issued by the salesman 'Paul Adam' from the orders table.

SELECT
    o.order_no,
    o.order_date,
    o.purch_amt,
    c.customer_name AS CustomerName,
    c.city AS CustomerCity
FROM [order] o
JOIN salesman s ON o.salesman_ID = s.salesman_id
JOIN customer c ON o.salesman_id = c.salesman_ID
WHERE s.Name = 'Paul Adam';

-- Que. 5. Display all the orders which values are greater than the
--  average order value for 10th October 2012.

SELECT *
FROM [order]
WHERE order_date = '2016-10-10'
AND purch_amt > (
    SELECT AVG(purch_amt)
    FROM [order] 
    WHERE order_date = '2016-10-10'
);

-- Que.6. Find all orders attributed to salesmen in Paris.

SELECT o.*, s.city AS SalesmanCity
FROM [order] o
JOIN salesman s ON o.salesman_id = s.salesman_ID
JOIN customer c ON o.customer_id = c.customer_id
WHERE s.city = 'Paris';

-- Que.7 Extract the data from the orders table for the salesman who earned the maximum commission.

SELECT o.*
FROM [order] o
WHERE o.salesman_id = (
    SELECT salesman_id
    FROM salesman
    WHERE Commission = (
        SELECT MAX(commission)
        FROM salesman
    )
);