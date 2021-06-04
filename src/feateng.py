import pandas as pd


"""
Create target as the mean between open and ajusted close.
"""
def create_target(data):
    data['Target'] = data[['Open', 'Adj Close']].mean(axis=1)
    return data
