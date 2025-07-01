from extract.extract_oltp import extract_orders, extract_customers, extract_products, extract_stores
from transform.star_transform import transform_to_star_schema

#Step-1: Extract
orders_df = extract_orders("2025-06-24 00:00:00")
customers_df = extract_customers()
products_df = extract_products()
stores_df = extract_stores()

#Step-2 : Transform
dim_customers, dim_products, dim_stores, dim_date, fact_orders = transform_to_star_schema(
    orders_df, customers_df, products_df, stores_df
)

print("Transform Done")
print("\n Fact Orders:\n", fact_orders.head())