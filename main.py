import pandas as pd
import matplotlib.pyplot as plt
from src.eda import show_overview, boxplot
from src.feateng import create_target
from src.preprocessing import normalize


def main():
    #Read data.
    data = pd.read_csv('GOOG.csv')
    data = data.set_index('Date')
    #Add target and normalize data.
    data = normalize(create_target(data))
    #Show overview
    show_overview(data) 
    #Show boxplot
    boxplot(data)
    plt.show()



if __name__ == '__main__':
    main()
