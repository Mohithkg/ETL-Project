from extract.extract_oltp import extract_orders, extract_customers, extract_products, extract_stores
from transform.star_transform import transform_to_star_schema
from load.snowflake_load import load_to_snowflake

#Step-1: Extract
orders_df = extract_orders("2025-06-24 00:00:00")
customers_df = extract_customers()
products_df = extract_products()
stores_df = extract_stores()

#Step-2 : Transform
dim_customers, dim_products, dim_stores, dim_date, fact_orders = transform_to_star_schema(
    orders_df, customers_df, products_df, stores_df
)

#Step-3 : Load to Snowflake
load_to_snowflake(dim_customers, "dim_customers")
load_to_snowflake(dim_products, "dim_products")
load_to_snowflake(dim_stores, "dim_stores")
load_to_snowflake(dim_date, "dim_date")
load_to_snowflake(fact_orders, "fact_orders")