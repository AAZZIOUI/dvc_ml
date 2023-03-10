import yaml
import os
#import pandas as pd

def read_yaml(path_to_yaml: str) -> dict :
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content

def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"directory created at {dir_path}")

def save_local_df(df,df_path, index_status=False):
    """
    We use this function to store train and test data
    args:
    df: is the dataframe we want to save/store
    df_path: is the path where we want to store the dataframe df
    """
    df.to_csv(df_path,index=index_status)
    print(f"data is saved at: {df_path}")
