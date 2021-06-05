import pandas as pd
import matplotlib.pyplot as plt
from src.eda import eda
from src.feateng import create_target
from src.preprocessing import normalize
from src.modelling import xgb, rf, svr, knnr


def main():
    #Read data.
    data = pd.read_csv('GOOG.csv')
    data = data.set_index('Date')
    #Add target and normalize data.
    data = normalize(create_target(data))
    #Divide data in features and target.
    x = data.loc[:, data.columns != 'Target']
    y = data['Target']
    print(x)
    print(y)
    #Run SUPERVISED models.
    print('XGB Starts')
    xgb(x,y)
    print('RF Starts')
    rf(x,y)
    print('SVR Starts')
    svr(x,y)
    print('KNN Starts')
    knnr(x,y)


if __name__ == '__main__':
    #df = pd.DataFrame(columns=['Model', 'MSE'])
    #df.to_csv('results.csv')
    main()
