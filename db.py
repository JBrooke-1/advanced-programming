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


def create_table(table_name, data_frame):
    if isinstance(data_frame, pd.DataFrame):
        result = data_frame.to_sql(table_name, connection, if_exists="append")
    metadata.create_all(engine)


def insert_data(table_name, data_frame, filepath="./data"):
    if isinstance(data_frame, pd.DataFrame):
        columns = list(data_frame.columns)
        filepath=f"./data/{table_name}.csv"
        # create a string from the columns that contains data
        column_string = str(columns).replace("[", "(").replace("]", ")")
        print(column_string)
        # create the table if it does not exist
        #create_table(table_name, column_string)
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


def create_table(table_name, columns):
    sql = text(
        f"""
        CREATE TABLE IF NOT EXISTS {table_name}
        {columns}
        """
    )
    print(sql)
    connection.execute(sql)


class Airport:
    id = Column(Integer, primary_key=True)
    ident = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Airport {self.id}>"
