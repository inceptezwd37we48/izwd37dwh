#python -m pip install pandas sqlalchemy pymysql
#python -m pip install --upgrade cryptography pymysql
import pandas as pd
from sqlalchemy import create_engine

username = 'root'
password = 'Root@1234'
host = '127.0.0.1'
db = 'stgdb'
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{db}")
folder="D:\\dataset\\"
table_file_dict = {
    "stg_transactions": folder+"transactions.csv",
    "stg_accounts": folder+"accounts.csv",
    "stg_payments": folder+"payments.csv",
    "stg_creditcard": folder+"creditcard.csv",
    "stg_loans": folder+"loans.csv",
    "stg_cust_profile": folder+"cust.csv",
    "stg_branches": folder+"branches.csv",
    "stg_employees": folder+"employee.csv"}

for table, file in table_file_dict.items():
    df = pd.read_csv(file)
    df.to_sql(table, con=engine, index=False, if_exists="replace")
    print(f"Rows loaded in the table {table}")