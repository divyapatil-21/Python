import urllib
from sqlalchemy import create_engine

def get_engine():
    server = "127.0.0.1"
    database = "restaurant_case_study"
    username = "sa"
    password = "Welcome#1"

    conn = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        f"Trusted_Connection=no;"
    )
    params = urllib.parse.quote_plus(conn)
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
    return engine

