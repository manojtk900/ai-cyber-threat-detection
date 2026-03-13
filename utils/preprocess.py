import pandas as pd
import numpy as np

def load_data(path):

    data = pd.read_csv(path)

    # remove spaces in column names
    data.columns = data.columns.str.strip()

    # convert label
    data['Label'] = data['Label'].apply(lambda x: 0 if x == "BENIGN" else 1)

    # replace infinite values
    data.replace([np.inf, -np.inf], np.nan, inplace=True)

    # fill missing values
    data.fillna(0, inplace=True)

    X = data.drop("Label", axis=1)
    y = data["Label"]

    return X, y