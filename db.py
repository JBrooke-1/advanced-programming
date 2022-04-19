# dbconnection with sqlalchemy
from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.
MYSQL_USER = os.getenv('MYSQL_USER', 'user')
DATABASE = os.getenv('DB_NAME', 'db')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'password')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_HOST = os.getenv('DB_HOST', 'localhost')
db_val = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}"
print(db_val)

engine = create_engine(
    db_val,
    echo=True, pool_recycle=3600)
connection = engine.connect()
metadata = MetaData()
ap = Table('airports', metadata, Column('id', Integer(), primary_key=True))
metadata.create_all(engine)


class Airport:
    id = Column(Integer, primary_key=True)
    ident = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Airport {self.id}>"
