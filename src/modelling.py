import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
import numpy as np


"""
Evaluate model using cross validation, 5 splits, 3 repeats.
"""
def evaluate(model, model_name, x, y):
    cv = RepeatedKFold(n_splits=5, n_repeats=3, random_state=42)
    score = np.mean(np.absolute(cross_val_score(model, x, y, scoring='neg_mean_squared_error', cv=cv, n_jobs=-1)))
    print(score)
    #Store result.
    res = pd.read_csv('results.csv')
    res['Model'] = res['Model'] + model_name
    res['MSE'] = res['MSE'] + score
    res.to_csv('results.csv')


def xgb(x,y):
    model = XGBRegressor()
    evaluate(model, 'XGBRegressor', x, y)
    

def rf(x,y):
    model = RandomForestRegressor()
    evaluate(model, 'RandomForestRegressor', x, y)


def svr(x,y):
    model = SVR()
    evaluate(model, 'SVR', x, y)


def knnr(x,y):
    model = KNeighborsRegressor()
    evaluate(model, 'KNNR', x, y)


