import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from src.eda import eda, target_lineplot
from src.feateng import create_target
from src.preprocessing import normalize
from src.modelling import xgb, rf, svr, knnr


def main():
    #Read data.
    data = pd.read_csv('GOOG.csv')
    data = data.set_index('Date')
    data.index = pd.to_datetime(data.index)
    #Add target and normalize data.
    data = normalize(create_target(data))
    #Divide data in features and target.
    last_train_date = np.datetime64('2018-01-01')
    print(type(data.index.values[0]))
    x_train = data.loc[:last_train_date, data.columns != 'Target']
    y_train = data.loc[:last_train_date, 'Target']
    x_test = data.loc[last_train_date:, data.columns != 'Target']
    y_test = data.loc[last_train_date:, 'Target']
    #Run SUPERVISED models.
    """
    print('XGB Starts')
    xgbpredictions = xgb(x_train,y_train,x_test,y_test)
    xgbpredictions = pd.DataFrame(xgbpredictions, columns=['Target'])
    xgbpredictions.index = y_test.index
    print(xgbpredictions)
    target_lineplot(xgbpredictions)

    print('RF Starts')
    rfpredictions = rf(x_train,y_train,x_test,y_test)
    rfpredictions = pd.DataFrame(rfpredictions, columns=['Target'])
    rfpredictions.index = y_test.index
    print(rfpredictions)
    target_lineplot(rfpredictions)

    print('SVR Starts')
    svrpredictions = svr(x_train,y_train,x_test,y_test)
    svrpredictions = pd.DataFrame(svrpredictions, columns=['Target'])
    svrpredictions.index = y_test.index
    print(svrpredictions)
    target_lineplot(svrpredictions)

    print('KNN Starts')
    knnpredictions = knnr(x_train,y_train,x_test,y_test)
    knnpredictions = pd.DataFrame(knnpredictions, columns=['Target'])
    knnpredictions.index = y_test.index
    print(knnpredictions)
    target_lineplot(knnpredictions)
    """


if __name__ == '__main__':
    #df = pd.DataFrame(columns=['Model', 'MSE'])
    #df.to_csv('results.csv')
    main()
