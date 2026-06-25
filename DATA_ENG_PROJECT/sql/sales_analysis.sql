SELECT SUM(total_revenue) AS total_revenue
FROM sales;


SELECT product, SUM(quantity) AS total_quantity
FROM sales
GROUP BY product
ORDER BY total_quantity DESC
LIMIT 5;

SELECT region, SUM(total_revenue) AS revenue
FROM sales
GROUP BY region;

SELECT 
MONTH(order_date) AS month,
SUM(total_revenue) AS revenue
FROM sales
GROUP BY month
ORDER BY month;