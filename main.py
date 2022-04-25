"""
STEP1: load the initial data set 
which consists of three CSV files 
and translate it into JSON format
"""
import matplotlib.pyplot as plt
from os import path, mkdir
import pandas as pd
import db
import os
from pathlib import Path


def read_csv_files(d_path="./data"):
    dfs_only = []
    dfs_dict = {}
    if os.path.isdir(d_path):
        dirs = [os.path.join(d_path, f) for f in os.listdir(d_path)]
        print(dirs)
        for file in dirs:
            if file.endswith(".csv"):
                val = pd.read_csv(file)
                dfs_only.append(val)
                key = Path(file).stem
                dfs_dict[key] = val
        return pd.concat(dfs_only), dfs_dict


all_df, df_dict = read_csv_files()

# export dataframes to json
print(df_dict["airports"])


def export_to_json():
    if not os.path.isdir("json_data"):
        mkdir("json_data")
    for key in df_dict:
        val = df_dict[key]
        file = f"./json_data/{key}.json"
        val.to_json(file)


# export file to json
export_to_json()

# populate the database
def populate_database():
    for key in df_dict:
        val = df_dict[key]
        db.insert_data(key, val)
        print(f"{key} table has been created successfully")


populate_database()

# plot some data

# plt.plot(airport_df["type"], airport_df["name"])
# plt.show()

# print(airport_df.to_html())
