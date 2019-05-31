import pandas as pd
from data_access import db_helper

def get_daily_adj_close(ticker):
    con = db_helper.get_con()
    sql = """SELECT sym.ticker,dp.price_date, dp.adj_close_price
    FROM securities_master.symbol AS sym
    INNER JOIN securities_master.daily_price AS dp
    ON dp.symbol_id = sym.id
    WHERE sym.ticker = '{}'
    ORDER BY dp.price_date ASC;""".format(ticker)
    return pd.read_sql_query(sql, con=con, index_col='price_date')

if __name__ == "__main__":
    print(get_daily_adj_close('MKC'))