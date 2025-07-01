import pandas as pd

def transform_to_star_schema(orders_df, customers_df, products_df, stores_df):
    #create dim_customers
    dim_customers = customers_df.copy()
    dim_customers['customer_sk'] = dim_customers.index + 1
    dim_customers = dim_customers[['customer_sk', 'customer_id','customer_name','email']]

    #create dim_products
    dim_products = products_df.copy()
    dim_products['product_sk'] = dim_products.index + 1
    dim_products = dim_products[['product_sk','product_id','product_name','category','price']]

    #create dim_stores
    dim_stores = stores_df.copy()
    dim_stores['stores_sk'] = dim_stores.index + 1
    dim_stores = dim_stores[['stores_sk','store_id','store_name','city']]

    #create dim_date
    orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
    dim_date = orders_df[['order_date']].drop_duplicates().reset_index(drop=True)
    dim_date['date_sk'] = dim_date.index + 1
    dim_date['year'] = dim_date['order_date'].dt.year
    dim_date['month'] = dim_date['order_date'].dt.month
    dim_date['day'] = dim_date['order_date'].dt.day

    #create fact_orders
    fact_orders = orders_df.copy()
    fact_orders = fact_orders.merge(dim_customers, on='customer_id') \
                             .merge(dim_products, on='product_id') \
                             .merge(dim_stores, on='store_id') \
                             .merge(dim_date, on='order_date')
    
    fact_orders = fact_orders[['order_id','customer_sk','product_sk',
    'stores_sk','date_sk','quantity','amount','order_date','updated_at'
    ]]

    return dim_customers, dim_date, dim_products, dim_stores, fact_orders
    
