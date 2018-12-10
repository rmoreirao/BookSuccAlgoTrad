from datetime import datetime

class DailyPrice:
    data_vendor_id: int
    symbol_id: int
    price_date: datetime
    created_date: datetime
    last_updated_date: datetime
    open_price: float
    high_price: float
    low_price: float
    close_price: float
    adj_close_price: float
    volume: float