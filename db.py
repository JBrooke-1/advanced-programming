# dbconnection with sqlalchemy
from sqlalchemy import create_engine, select, MetaData, Table

engine = create_engine("sqlite:///database.db?check_same_thread=False", echo=True)
connection = engine.connect()
