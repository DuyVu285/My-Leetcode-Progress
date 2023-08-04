# Write your MySQL query statement below
SELECT distinct SalesPerson.name
FROM SalesPerson
LEFT JOIN Orders ON SalesPerson.sales_id = Orders.sales_id
where SalesPerson.sales_id not in (
    select distinct Orders.sales_id from Orders
    LEFT JOIN Company ON Company.com_id = Orders.com_id
    WHERE Company.name = "RED"
);
