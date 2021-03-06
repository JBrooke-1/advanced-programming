"""
STEP1: load the initial data set 
which consists of three CSV files 
and translate it into JSON format
"""
from os import path, mkdir
import pandas as pd
import db
import os
from pathlib import Path
import logging
import time
import shutil


def clean_data(d_path="./data", c_path="./data_cleaned"):
    # create cleaned file path if not exist already
    if not os.path.isdir(c_path):
        os.makedirs(c_path)

        # copy files from data folder to new folder
        if os.path.isdir(d_path):
            for f_name in os.listdir(d_path):
                dest_path = c_path + "/" + f_name
                s_path = d_path + "/" + f_name
                print(dest_path, s_path)
                if os.path.isfile(s_path):
                    shutil.copy(s_path, dest_path)
                    print(f"copied {s_path} to {dest_path}")

        if os.path.isdir(c_path):
            dirs = [os.path.join(c_path, f) for f in os.listdir(c_path)]
            for file in dirs:
                print(file)
                if file.endswith(".csv"):
                    with open(file, "r+", encoding="utf-8") as csv_file:
                        content = csv_file.read()
                    with open(file, "w+", encoding="utf-8") as csv_file:
                        csv_file.write(content.replace('"', ''))
                    csv_file.close()


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


clean_data()
all_df, df_dict = read_csv_files()


def export_to_json():
    if not os.path.isdir("json_data"):
        mkdir("json_data")
    for key in df_dict:
        val = df_dict[key]
        file = f"./json_data/{key}.json"
        val.to_json(file)


# export file to json
export_to_json()

# create all trables


def create_tables():
    for key in df_dict:
        val = df_dict[key]
        print(f"{key} : {val}")
        db.create_tables(key, val)


# populate the database
def populate_database():
    threads = list()
    for key in df_dict:
        val = df_dict[key]
        print(f"{key} : {val}")
        db.insert_data(key, val)
        # x = threading.Thread(target=db.insert_data, args=(key, val), daemon=True)
        # x.start()
        # threads.append(x)
        time.sleep(0.1)

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)


create_tables()
populate_database()
