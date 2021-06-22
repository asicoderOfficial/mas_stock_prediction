import re
from yahoofinancials import YahooFinancials
import numpy as np

class Yahoo:
    """
    Class for getting technical and fundamental data from YahooFinance,
    using the library yahoofinancials: https://github.com/JECSand/yahoofinancials
    TODO: finish constructor, test, and implement methods.
    """
    #YYYY-MM-DD pattern for start and end.
    DATES_PATTERN = re.compile('/^\d{4}-\d{2}-\d{2}$/')
    #Possible frequencies and statements.
    freqs = {'annual', 'quarterly'}
    statements = {'income', 'balance', 'cash'}
    intervals = {'daily', 'weekly', 'monthly'}
    price_types = {'current', 'average'}

    def __init__(self, ticker: str, **kwargs):
        if ('start' in kwargs and type(kwargs['start']) != str) or ('end' in kwargs and type(kwargs['end']) != str):
            raise ValueError('"start" and "end" parameters must be of type "str"')
        if 'freq' in kwargs and (type(kwargs['freq']) != str or kwargs['freq'] not in Yahoo.freqs): 
            raise ValueError('"freq" must be of type "str", and either "annual" or "quarterly"')
        if 'reformat' in kwargs and type(kwargs['reformat']) != bool:
            raise ValueError('"reformat" must be bool')
        if 'start' in kwargs and not DATES_PATTERN.search(kwargs['start']):
            raise ValueError('"start" must follow YYYY-MM-DD format')
        if 'end' in kwargs and not DATES_PATTERN.search(kwargs['end']):
            raise ValueError('"end" must follow YYYY-MM-DD format')
        if 'start' in kwargs and not 'end' in kwargs:
            raise ValueError('"start" was passed, but "end" was missing')
        if 'end' in kwargs and not 'start' in kwargs:
            raise ValueError('"end" was passed, but "start" wass missing')
        if 'time_interval' in kwargs and (type(kwargs['time_interval']) != str or kwargs['time_interval'] not in Yahoo.intervals):
            raise ValueError('"time_interval" must be of type "str" and either "daily", "weekly" or "monthly"')
        if 'statement_type' in kwargs and (type(kwargs['statement_type']) != str or kwargs['statement_type'] not in Yahoo.statements):
            raise ValueError('"statement_type" must be of type "str" and either "income", "balance" or "cash"')
        if 'price_type' in kwargs and (type(kwargs['price_type']) != str or kwargs['price_type'] not in Yahoo.statements):
            raise ValueError('"price_type" must be of type "str" and either "current" or "average"')

        self.ticker = ticker
        self.yf_obj = YahooFinancials(self.ticker)

        if 'start' in kwargs:
            self.start = kwargs['start']
        if 'end' in kwargs:
            self.end = kwargs['end']
        if 'freq' in kwargs:
            self.freq = kwargs['freq']
        if 'reformat' in kwargs:
            self.reformat = kwargs['reformat']
        if 'time_interval' in kwargs:
            self.time_interval = kwargs['time_interval']
        if 'statement_type' in kwargs:
            self.statement_type = kwargs['statement_type']
        if 'price_type' in kwargs:
            self.price_type = kwargs['price_type']

