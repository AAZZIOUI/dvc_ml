import os
from src.utils.all_utils import read_yaml
import argparse
import pandas as pd
from sklearn.linear_model import ElasticNet

def train(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # save dataset in local directory

    artifacts_dir = config["artifacts"]["artifacts_dir"]
    split_data_dir = config["artifacts"]["split_data_dir"]

    train_data_filename = config["artifacts"]["train"]

    train_data_path = os.path.join(artifacts_dir, split_data_dir, train_data_filename)

    df_train_data = pd.read_csv(train_data_path)

    train_y = df_train_data["quality"]
    train_x = df_train_data.drop("quality", axis=1)

    alpha = params["model_params"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = params["model_params"]["ElasticNet"]["params"]["l1_ratio"]
    random_state = params["model_params"]["ElasticNet"]["params"]["random_state"]

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    lr.fit(train_x,train_y)
    print ("Done")


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")


    parsed_args = args.parse_args()

    train(config_path=parsed_args.config, params_path= parsed_args.params)