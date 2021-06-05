import pandas as pd
import matplotlib.pyplot as plt


def show_overview(data):
    #DataFrame shape.
    print('Shape of DataFrame is: {}\n'.format(str(data.shape)))
    #First 10 rows.
    print('First 10 rows look like this:')
    print(data.head(10))
    #Stats.
    print('\nDataframe stats are:')
    print(data.describe())


"""
Create boxplot of all, or selected columns.
"""
def boxplot(data, columns=[]):
    if columns == []:
        data.plot.box()
    else:
        data[columns].plot.box()
    plt.show()


"""
Create lineplot of target through time.
"""
def target_lineplot(data):
    data['Target'].plot()
    plt.show()



"""
Invoke all eda
"""
def eda(data, columns=[]):
    show_overview(data)
    boxplot(data, columns)
    target_lineplot(data)

