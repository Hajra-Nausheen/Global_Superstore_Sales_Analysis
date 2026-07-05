CREATE TABLE global_superstore (
    category TEXT,
    city TEXT,
    country TEXT,
    customer_id TEXT,
    customer_name VARCHAR(100),
    discount DECIMAL(5,2),
    market TEXT,
    order_date DATE,
    order_id TEXT,
    order_priority TEXT,
    product_id TEXT,
    product_name TEXT,
    profit DECIMAL(10,2),
    quantity INT,
    region TEXT,
    row_id INT,
    sales DECIMAL(10,2),
    segment TEXT,
    ship_date DATE,
    ship_mode TEXT,
    shipping_cost DECIMAL(10,2),
    state TEXT,
    sub_category TEXT,
    year INT,
    market2 TEXT,
    weeknum INT,
    order_year INT,
    order_month VARCHAR(10),
    order_month_num INT,
    order_quarter INT,
    shipping_days INT,
    profit_margin DECIMAL(10,2)
);
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
