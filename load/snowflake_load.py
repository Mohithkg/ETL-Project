import snowflake.connector
import pandas as pd
import yaml

def get_snowflake_connection():
    with open("config/db_config.yaml", "r") as file:
        config = yaml.safe_load(file)

    sf_cfg = config["snowflake"]

    conn = snowflake.connector.connect(
        user=sf_cfg["user"],
        password=sf_cfg["password"],
        account=sf_cfg["account"],
        warehouse=sf_cfg["warehouse"],
        database=sf_cfg["database"],
        schema=sf_cfg["schema"]
    )
    return conn

def load_to_snowflake(df, table_name):
    conn = get_snowflake_connection()
    cursor = conn.cursor()

    try:
        # Drop and recreate the table (basic schema inference from df)
        columns = ", ".join([f'"{col}" STRING' for col in df.columns])
        cursor.execute(f'CREATE OR REPLACE TABLE {table_name} ({columns})')

        # Upload rows using INSERT INTO
        for _, row in df.iterrows():
            values = ", ".join([f"'{str(v)}'" if pd.notnull(v) else "NULL" for v in row])
            insert_query = f'INSERT INTO {table_name} VALUES ({values})'
            cursor.execute(insert_query)

        print(f"✅ Loaded {len(df)} rows into {table_name} using Snowflake Connector.")
    finally:
        cursor.close()
        conn.close()

