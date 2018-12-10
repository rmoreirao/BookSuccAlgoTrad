from datetime import datetime

import pathlib
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd


from quote_fetcher.Quote import Quote

COL_DATE = 'date'
COL_OPEN = '1. open'
COL_HIGH = '2. high'
COL_LOW = '3. low'
COL_CLOSE = '4. close'
COL_ADJ_CLOSE = '5. adjusted close'
COL_VOL = '6. volume'
COL_DIV = '7. dividend amount'
COL_SPLIT = '8. split coefficient'
COL_SYMBOL = 'symbol'

def get_historical_daily_quotes_df(symbol:str):
    ts = TimeSeries(key='ZXTHHYQU7E5O8R75', output_format='pandas')
    df, meta_data = ts.get_daily_adjusted(symbol=symbol, outputsize='full')
    return df

def get_historical_daily_quotes_array(symbol:str):
    df = get_historical_daily_quotes_df(symbol)
    quotes = []
    for index, row in df.iterrows():
        quote = Quote()
        quote.adj_close_price = row[COL_ADJ_CLOSE]
        quote.close_price = row[COL_CLOSE]
        quote.high_price = row[COL_HIGH]
        quote.low_price = row[COL_LOW]
        quote.open_price = row[COL_OPEN]
        quote.volume = row[COL_VOL]
        quote.price_date = index
        quotes.append(quote)

    return quotes


def test_get_historical_daily_quotes():
    symbol = 'AAPL'
    get_historical_daily_quotes_array(symbol)

if __name__ == "__main__":
    test_get_historical_daily_quotes()