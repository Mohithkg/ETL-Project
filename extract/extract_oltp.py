import psycopg2
import pandas as pd
import yaml
from sqlalchemy import create_engine


def load_config():
    with open('config/db_config.yaml','r') as file:
        return yaml.safe_load(file)
        
def getconnection():
    #conn = psycopg2.connect()
    config = load_config()
    pg_cfg = config['postgres']
    host = pg_cfg['host']
    port = str(pg_cfg['port'])
    database = pg_cfg['database']
    user = pg_cfg['user']
    password = pg_cfg['password']
    engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
    return engine

def extract_orders(last_updated_timestamp):
    conn = getconnection()
    query = f"""SELECT * FROM orders
            WHERE updated_at > '{last_updated_timestamp}'"""
    df = pd.read_sql(query,conn)
    #conn.close()
    return df

def extract_customers():
    conn = getconnection()
    query = "SELECT * FROM customers"
    df = pd.read_sql(query, conn)
    #conn.close()
    return df

def extract_products():
    conn = getconnection()
    query = "SELECT * FROM products"
    df = pd.read_sql(query,conn)
    #conn.close()
    return df

def extract_stores():
    conn = getconnection()
    query = "SELECT * FROM stores"
    df = pd.read_sql(query,conn)
    #conn.close()
    return df
