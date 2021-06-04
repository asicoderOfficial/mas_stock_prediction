import pandas as pd
from sklearn.preprocessing import MinMaxScaler


"""
Normalize data, min max way.
"""
def normalize(data):
    data[data.columns] = MinMaxScaler().fit_transform(data[data.columns])
    return data
