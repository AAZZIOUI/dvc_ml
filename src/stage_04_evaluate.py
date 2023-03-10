import os
from src.utils.all_utils import read_yaml, create_directory, save_reports
import argparse
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
def evaluate_metrics(actual_values, predicted_values):
    rmse = np.sqrt(mean_squared_error(actual_values,predicted_values))
    mae = mean_absolute_error(actual_values,predicted_values)
    r2 = r2_score(actual_values,predicted_values)
    return rmse, mae, r2


def evaluate(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    # save dataset in local directory

    artifacts_dir = config["artifacts"]["artifacts_dir"]
    split_data_dir = config["artifacts"]["split_data_dir"]

    test_data_filename = config["artifacts"]["test"]

    test_data_path = os.path.join(artifacts_dir, split_data_dir, test_data_filename)

    df_train_data = pd.read_csv(test_data_path)

    test_y = df_train_data["quality"]
    test_x = df_train_data.drop("quality", axis=1)


    model_dir = config["artifacts"]["model_dir"]
    model_filename = config["artifacts"]["model_filename"]
    model_path = os.path.join(artifacts_dir,model_dir, model_filename)
    lr = joblib.load(model_path)

    predicted_value = lr.predict(test_x)
    rmse, mae, r2 = evaluate_metrics(test_y, predicted_value)

    reports_dir = config["artifacts"]["reports_dir"]
    scores_filename = config["artifacts"]["scores"]
    reports_dir_path = os.path.join(artifacts_dir, reports_dir)
    create_directory([reports_dir_path])
    scores_filepath = os.path.join(reports_dir_path,scores_filename)

    scores_dict = {"rmse":rmse, "mae":mae, "r2":r2}
    save_reports(report = scores_dict, report_path= scores_filepath)

if __name__ == '__main__':
    args = argparse.ArgumentParser()
    
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")


    parsed_args = args.parse_args()

    evaluate(config_path=parsed_args.config, params_path= parsed_args.params)