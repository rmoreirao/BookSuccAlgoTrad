from __future__ import print_function

from quote_fetcher import quote_fetcher_alpha_vantage
import datetime
import warnings
import MySQLdb as mdb
import requests
# Obtain a database connection to the MySQL instance
db_host = 'localhost'
db_user = 'sec_user'
db_pass = 'password'
db_name = 'securities_master'
con = mdb.connect(db_host, db_user, db_pass, db_name)
def obtain_list_of_db_tickers_not_loaded():
    """
    Obtains a list of the ticker symbols in the database.
    """
    with con:
        cur = con.cursor()
        # Fetch all the symbols which are not on the database already
        cur.execute("SELECT id, ticker FROM symbol sym where sym.id not in (select symbol_id from securities_master.daily_price)")
        data = cur.fetchall()
        return [(d[0], d[1]) for d in data]

def get_daily_historic_data_from_alpha_vantage(ticker):
    try:
        return quote_fetcher_alpha_vantage.get_historical_daily_quotes_array(ticker)
    except Exception as e:
        print("Could not download data for {}: {}".format(ticker,e))
        return None
    return prices

def insert_daily_data_into_db(data_vendor_id, symbol_id, quotes):
    """
    Takes a list of tuples of daily data and adds it to the
    MySQL database. Appends the vendor ID and symbol ID to the data.
    daily_data: List of tuples of the OHLC data (with
    adj_close and volume)
    """
    # Create the time now
    now = datetime.datetime.utcnow()
    # Amend the data to include the vendor ID and symbol ID
    daily_data = [
    (data_vendor_id, symbol_id, quote.price_date, now, now,
     quote.open_price, quote.high_price, quote.low_price, quote.close_price, quote.volume, quote.adj_close_price)
    for quote in quotes
    ]
    # Create the insert strings
    column_str = """data_vendor_id, symbol_id, price_date, created_date,
    last_updated_date, open_price, high_price, low_price,
    close_price, volume, adj_close_price"""
    insert_str = ("%s, " * 11)[:-2]
    final_str = "INSERT INTO daily_price (%s) VALUES (%s)" % \
    (column_str, insert_str)
    # Using the MySQL connection, carry out an INSERT INTO for every symbol
    with con:
        cur = con.cursor()
        cur.executemany(final_str, daily_data)

if __name__ == "__main__":

    # Loop over the tickers and insert the daily historical
    # data into the database
    tickers = obtain_list_of_db_tickers_not_loaded()
    lentickers = len(tickers)
    for i, t in enumerate(tickers):
        print("Adding data for %s: %s out of %s" %
            (t[1], i+1, lentickers))
        quotes = get_daily_historic_data_from_alpha_vantage(t[1])
        if quotes:
            insert_daily_data_into_db('1', t[0], quotes)

    print("Finished adding pricing data to DB.")
