import pandas as pd
import MySQLdb as mdb

from data_access import db_helper

def get_daily_adj_close():
    COL_PRICE_DATE = "price_date"
    COL_ADJ_CLOSE_PRICE = "adj_close_price"

    def query(self,ticker):
        con = db_helper.get_con()
        sql = """SELECT dp.{}, dp.{}
        FROM symbol AS sym
        INNER JOIN daily_price AS dp
        ON dp.symbol_id = sym.id
        WHERE sym.ticker = {}
        ORDER BY dp.price_date ASC;""".format(self.COL_PRICE_DATE,self.COL_ADJ_CLOSE_PRICE, ticker)
        return pd.read_sql_query(sql, con=con, index_col='price_date')

if __name__ == "__main__":
    print(get_daily_adj_close('AAPL'))