'''
STEP1: load the initial data set 
which consists of three CSV files 
and translate it into JSON format
'''
import pandas as pd
airport_df = pd.read_csv("./data/airports.csv")
airport_frequencies_df = pd.read_csv("./data/airport-frequencies.csv")
runways_df = pd.read_csv("./data/runways.csv")

# export dataframes to json
from os import path, mkdir
if not path.isdir('json_data'):
    mkdir('json_data')
airport_df.to_json(r'./json_data/airport.json')

# connect to sqllite, a built in python module
import sqlite3
#create db connection
conn = sqlite3.connect('data.db')
# execute some sql command
c = conn.cursor()
