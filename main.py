'''
STEP1: load the initial data set 
which consists of three CSV files 
and translate it into JSON format
'''
import pandas as pd
airport_df = pd.read_csv("./data/airports.csv")
airport_frequencies_df = pd.read_csv("./data/airport-frequencies.csv")
runways_df = pd.read_csv("./data/runways.csv")
