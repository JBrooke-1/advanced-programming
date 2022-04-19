'''
STEP1: load the initial data set 
which consists of three CSV files 
and translate it into JSON format
'''
import pandas as pd
airport_df = pd.read_csv("./data/airports.csv")
airport_frequencies_df = pd.read_csv("./data/airport-frequencies.csv")
runways_df = pd.read_csv("./data/runways.csv")

# debug column infos
print(airport_df.columns)
print(airport_frequencies_df.columns)
print(runways_df.columns)


# debug critical classes
print(airport_df.head(30)["type"])

