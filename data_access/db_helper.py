import MySQLdb as mdb

# Connect to the MySQL instance
db_host = 'localhost'
db_user = 'sec_user'
db_pass = 'password'
db_name = 'securities_master'

def get_con():
    return mdb.connect(db_host, db_user, db_pass, db_name)
