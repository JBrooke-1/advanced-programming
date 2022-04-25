# dbconnection with sqlalchemy
from sqlalchemy import (
    create_engine,
    select,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    text,
)
from dotenv import load_dotenv
import os
import pandas as pd
from pandas.api.types import is_string_dtype
import numpy as np

load_dotenv()  # take environment variables from .env.
MYSQL_USER = os.getenv("MYSQL_USER", "user")
DATABASE = os.getenv("DB_NAME", "db")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "password")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_HOST = os.getenv("DB_HOST", "localhost")
db_val = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}?charset=utf8&local_infile=1"
print(db_val)

engine = create_engine(db_val, echo=True)
connection = engine.connect()
metadata = MetaData()


def create_table_and_insert_data(table_name, data_frame):
    if isinstance(data_frame, pd.DataFrame):
        result = data_frame.to_sql(
            table_name, connection, if_exists="append", method="multi"
        )
        metadata.create_all(engine)
        print(f"{table_name} table has been created successfully")
    else:
        print("error you need to pass in dataframe")


def insert_data(table_name, data_frame, filepath="./data"):
    if isinstance(data_frame, pd.DataFrame):
        columns = list(data_frame.columns)
        filepath = f"./data/{table_name}.csv"
        # create a string from the columns that contains data
        column_string = str(columns).replace("[", "(").replace("]", ")")
        print(column_string)
        # create the table if it does not exist
        # create_table(table_name, column_string)
        sql = text(
            f"""
            LOAD DATA LOCAL INFILE '{filepath}' 
            INTO TABLE {table_name}
            FIELDS TERMINATED BY ','
            IGNORE 1 LINES 
            {column_string}
            """
        )
        connection.execute(sql)

def create_tables(table_name, df):
    if isinstance(df, pd.DataFrame):
        final_column = format_columns(df)
        sql = text(
            f"""
            CREATE TABLE IF NOT EXISTS `{table_name}`
            (
              {final_column}
            )
            """
        )
        print(sql)
        connection.execute(sql)

def format_columns(df):
    columns = df.dtypes.to_dict()
    print(columns)
    for key, val in columns.items():
        print(key, val)
        if is_string_dtype(val):
            columns[key] = "varchar(255)"
        else:
            if val == np.float64:
                columns[key] = "float"
            elif val == np.int64:
                columns[key] = "int"
            else:
                print("error datatype not found")
                return
    print(columns)
    final_column = ""
    for key, val in columns.items():
        if key != list(columns)[-1]:
            final_column += f"{key} {val},\n"
        else:
            final_column += f"{key} {val}"
    print(final_column)
    return final_column


class Airport:
    id = Column(Integer, primary_key=True)
    ident = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Airport {self.id}>"
