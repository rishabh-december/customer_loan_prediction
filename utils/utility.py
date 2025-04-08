import os
import pandas as pd

def load_dataset(base_path, data):

    print("------File reading Started------")
    file_ = os.path.join(base_path, data)
    if file_.split(".")[-1] == "csv":
        df = pd.read_csv(file_)
    else:
        df = pd.read_excel(file_)
    # df_var_describe = pd.read_excel(base_path + data_dict)
    print("------File reading completed------")

    # df_var_describe = pd.read_excel(base_path + data_dict)
    # label_dict = pd.Series(df_var_describe.Var.values,index=df_var_describe.Var).to_dict()
    
    return df