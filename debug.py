"""
STEP1: load the initial data set 
which consists of three CSV files 
and translate it into JSON format
"""
from lib2to3.pgen2.pgen import DFAState
import pandas as pd

airport_df = pd.read_csv("./data/airports.csv")
airport_frequencies_df = pd.read_csv("./data/airport-frequencies.csv")
runways_df = pd.read_csv("./data/runways.csv")

# debug column infos
print(airport_df.columns)
print(airport_frequencies_df.columns)
print(runways_df.columns)

# debug airport data usage
airport_memory = airport_df.memory_usage(index=False, deep=True)
airport_columns = list(airport_df.columns)
print(airport_memory['id'].max() >> 125)
print(airport_df.dtypes)
print("airport memory used a total of : ", airport_memory.sum(), " bytes")
