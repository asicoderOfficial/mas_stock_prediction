import pandas as pd
from src.eda import show_overview


def main():
    #Read data.
    data = pd.read_csv('GOOG.csv')
    #Show overview
    show_overview(data) 


if __name__ == '__main__':
    main()
