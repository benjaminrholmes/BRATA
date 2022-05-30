import pymysql
import pandas as pd
import sqlalchemy

# # Credentials to database connection
hostname = "localhost"
dbname = "brata"
uname = "root"
pwd = "DEVINA187"

local_connection = pymysql.connect(host=hostname,
                                   user=uname,
                                   password=pwd,
                                   db=dbname)

fbref_connection = pymysql.connect(host=hostname,
                                   user=uname,
                                   password=pwd,
                                   db="fbref")

pd_engine = sqlalchemy.create_engine("mysql+pymysql://{user}:{password}@{host}/{db}".format(user=uname,
                                                                                            password=pwd,
                                                                                            host=hostname,
                                                                                            db=dbname))


def fetch_mysql(sql_query):
    cursor = local_connection.cursor()
    cursor.execute(sql_query)
    result_sql = cursor.fetchall()
    return result_sql


def fetch_fbref_mysql(sql_query):
    cursor = fbref_connection.cursor()
    cursor.execute(sql_query)
    result_sql = cursor.fetchall()
    return result_sql


def convert_mysql_pd(sql_query):
    pandas_df = pd.read_sql(sql_query, pd_engine)
    return pandas_df
