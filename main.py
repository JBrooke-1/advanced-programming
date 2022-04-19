"""
STEP1: load the initial data set 
which consists of three CSV files 
and translate it into JSON format
"""
import pandas as pd

airport_df = pd.read_csv("./data/airports.csv")
airport_frequencies_df = pd.read_csv("./data/airport-frequencies.csv")
runways_df = pd.read_csv("./data/runways.csv")

# export dataframes to json
from os import path, mkdir

if not path.isdir("json_data"):
    mkdir("json_data")
airport_df.to_json(r"./json_data/airport.json")

# connect to sqllite, a built in python module
import sqlite3

# dbconnection with sqlalchemy
from sqlalchemy import create_engine
engine = create_engine('sqlite:///database.db', echo=True)
sqlite_connection = engine.connect()
airport_sqlite_table = "airports"

# write data into database
airport_df.to_sql(airport_sqlite_table, sqlite_connection,if_exists='fail')
sqlite_connection.close() # close db

# plot some data
import matplotlib.pyplot as plt

plt.plot(airport_df["type"], airport_df["name"])
plt.show()

print(airport_df.to_html())