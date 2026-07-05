SELECT * FROM global_superstore;

-- Total Profit
select Round(sum(profit),2) AS total_profit
from global_superstore;

-- Total Sales
select Round(sum(sales),2) AS total_sales
from global_superstore;

-- Total Shipping Cost
select Round(sum(shipping_cost),2) AS total_shipping_cost
from global_superstore;

-- Total countries
select count(distinct country) AS total_countries
from global_superstore;

-- Total orders
select count(distinct order_id ) AS total_orders
from global_superstore;

-- Total customers
select count(distinct customer_id) AS total_countries
from global_superstore;