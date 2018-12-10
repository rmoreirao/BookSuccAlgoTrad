from __future__ import print_function
import datetime
from math import ceil
import bs4
import MySQLdb as mdb
import requests
import pandas as pd


def obtain_parse_wiki_snp500():

    symbols_table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies",
                                 header=0)[0]
    now = datetime.datetime.utcnow()
    symbols = []
    for index, row in symbols_table.iterrows():
        symbols.append(
            (
                row['Symbol'],  # Ticker
                'stock',
                row['Security'],  # Name
                row['GICS Sector'],  # Sector
                'USD', now, now
            )
        )

    return symbols


def insert_snp500_symbols(symbols):
    """
    Insert the S&P500 symbols into the MySQL database.
    """
    # Connect to the MySQL instance
    db_host = 'localhost'
    db_user = 'sec_user'
    db_pass = 'password'
    db_name = 'securities_master'
    con = mdb.connect(
        host=db_host, user=db_user, passwd=db_pass, db=db_name
    )
    # Create the insert strings
    column_str = """ticker, instrument, name, sector,
    currency, created_date, last_updated_date
    """
    insert_str = ("%s, " * 7)[:-2]
    final_str = "INSERT INTO symbol (%s) VALUES (%s)" % \
                (column_str, insert_str)
    # Using the MySQL connection, carry out
    # an INSERT INTO for every symbol
    with con:
        cur = con.cursor()
        cur.executemany(final_str, symbols)


if __name__ == "__main__":
    symbols = obtain_parse_wiki_snp500()
    insert_snp500_symbols(symbols)
    print("%s symbols were successfully added." % len(symbols))
