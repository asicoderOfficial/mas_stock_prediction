import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
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


"""
Supervised learning algorithms.
"""
def xgb(x_train,y_train, x_test, y_test):
    model = XGBRegressor()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    print(mean_squared_error(y_test, predictions))
    predictions = pd.DataFrame(predictions)
    predictions.to_csv('XGBPredictions.csv')
    return predictions
    

def rf(x_train,y_train, x_test, y_test):
    model = RandomForestRegressor()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    print(mean_squared_error(y_test, predictions))
    predictions = pd.DataFrame(predictions)
    predictions.to_csv('RFPredictions.csv')
    return predictions


def svr(x_train,y_train, x_test, y_test):
    model = SVR()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    print(mean_squared_error(y_test, predictions))
    predictions = pd.DataFrame(predictions)
    predictions.to_csv('SVRPredictions.csv')
    return predictions


def knnr(x_train,y_train, x_test, y_test):
    model = KNeighborsRegressor()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    print(mean_squared_error(y_test, predictions))
    predictions = pd.DataFrame(predictions)
    predictions.to_csv('KNNRPredictions.csv')
    return predictions



"""
Reinforcement learning algorithms.
"""
def rl(

