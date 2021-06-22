import numpy as np
import pandas as pd
import io
import requests


class Alpha:
    """
    Parent class for getting data from AlphaVantage API.
    """
    def __init__(self, ticker: str, apikey:str): 
        """
        Args:
            ticker (str): Ticker for the company to retrieve data from.
            apikey (str): The API key to be used for the request.
        """
        if type(ticker) != str: 
            raise ValueError('"ticker" must be of type "str"')
        if type(apikey) != str: 
            raise ValueError('"apikey" must be of type "str"')
        self.ticker = ticker
        self.apikey = apikey


class DailyTechAlpha(Alpha):
    """
    Alpha's child class for getting daily technical data
    """
    OUTPUTSIZES = {'compact', 'full'}

    def __init__(self, ticker:str, apikey:str, outputsize:str='compact'):
        """
        Args:
            ticker, apikey: initialized by parent class Alpha.
            outputsize (str): Period to get data.
                                #compact: default value, latest 100 data points.
                                #full: all the history.
        """
        super().__init__(ticker, apikey)
        if type(outputsize) != str:
            raise ValueError('"outputsize" must be of type "str"')
        if outputsize not in DailyTechAlpha.OUTPUTSIZES:
            raise ValueError('"outputsize" must be either "compact" or "full"')
        self.outputsize = outputsize
        self.function = 'TIME_SERIES_DAILY'
        self.datatype = 'csv'

   
    def get_df(self):
        """
        Returns the DataFrame for the current class attributes' values,
        indexed by date.
        """
        url = 'https://www.alphavantage.co/query?function={}&symbol={}&datatype={}&apikey={}'.format(self.function, self.ticker, self.datatype, self.apikey)
        r = requests.get(url)
        return pd.read_csv(io.StringIO(r.text)).set_index('timestamp')
        

class FundAlpha(Alpha):
    """
    Alpha's child class for getting quarterly fundamental data.
    It combines reports for: earnings, income statement, balance sheet and cash flow.
    """
    def __init__(self, ticker:str, apikey:str):
        """
        Args:
            ticker, apikey: initialized by parent class Alpha.
        functions (list): it contains the list of functions to traverse for doing all the API calls.
        """
        super().__init__(ticker, apikey)
        self.functions = ['EARNINGS', 'INCOME_STATEMENT', 'BALANCE_SHEET', 'CASH_FLOW']

    
    def get_df(self):
        """
        Iterates all self.functions and combines them in the same DataFrame.
        Returns:
        pandas.DataFrame: combination of functions, indexed by timestamp.
        """
        final_df = pd.DataFrame();
        for function in self.functions:
            url = 'https://www.alphavantage.co/query?function={}&symbol={}&apikey={}'.format(function, self.ticker, self.apikey)
            r = requests.get(url)
            curr_df = pd.DataFrame(r.json()[list(r.json().keys())[2]])
            #Store only columns that have not already appeared in previous queries.
            curr_df = curr_df[curr_df.columns.difference(final_df.columns)]
            if not final_df.empty:
                final_df = final_df.merge(curr_df, left_index=True, right_index=True)
            else:
                final_df = pd.concat([final_df, curr_df])
        return final_df.set_index('fiscalDateEnding')


