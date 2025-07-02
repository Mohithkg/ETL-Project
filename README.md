
# Snowflake ETL Project

This project demonstrates how to load Pandas DataFrames into Snowflake using the **Snowflake Connector for Python**, without SQLAlchemy.

## 📦 Project Structure

```
etl_project/
├── config/
│   └── db_config.yaml
├── env/                         # Virtual environment (excluded from version control)
├── extract/
│   └── extract_oltp.py
├── load/
│   └── snowflake_load.py
├── logs/
│   └── log_file.log             # (or similar log files)
├── transform/
│   └── transform_data.py
├── main.py
├── requirements.txt
└── README.md

---

## 🧰 Requirements

- Python 3.7+
- Packages:
  - `pandas`
  - `snowflake-connector-python`
  - `pyyaml`

Install them using pip:

```bash
pip install pandas snowflake-connector-python pyyaml
```

---

## 🔐 Configuration

Edit `config/db_config.yaml` to include your Snowflake credentials:

```yaml
postgres:
  host: YOUR_HOST
  port: 5432
  database: DB_NAME
  user: DB_USER
  password: DB_PASSWORD

snowflake:
  user: YOUR_USERNAME
  password: YOUR_PASSWORD
  account: YOUR_ACCOUNT_ID
  warehouse: YOUR_WAREHOUSE
  database: YOUR_DATABASE
  schema: YOUR_SCHEMA
```

---

## 🚀 Usage

1. Prepare your DataFrame in `main.py`.
2. Call `load_to_snowflake(df, "table_name")` to load it to the specified Snowflake table.

Example:

```python
from load.snowflake_load import load_to_snowflake
import pandas as pd

df = pd.DataFrame({
    "id": [1, 2],
    "name": ["Apple", "Banana"]
})

load_to_snowflake(df, "products")
```

---

## ❗ Troubleshooting

- ✅ **Loaded to wrong table?** Make sure you're passing the correct `table_name` to `load_to_snowflake`.
- ✅ **Rename a table:**  
  ```sql
  ALTER TABLE old_table_name RENAME TO new_table_name;
  ```
- ✅ **Connection Error:** Ensure credentials in `db_config.yaml` are valid and the Snowflake account is accessible.

---

## 📞 Support

For any issues, please raise a GitHub issue.
