from pydataset import data
from db import pd_engine
from fbref_scrape import merged_test8
import sqlalchemy

# # Credentials to database connection
hostname = "localhost"
dbname = "fbref"
uname = "root"
pwd = "DEVINA187"

fbref_engine = sqlalchemy.create_engine("mysql+pymysql://{user}:{password}@{host}/{db}".format(user=uname,
                                                                                               password=pwd,
                                                                                               host=hostname,
                                                                                               db=dbname))

iris = data('iris')


def send_pd_sql(panda_df, table_name, engine):
    panda_df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    print("DONE")
    return


# send_pd_sql(iris, "iris", engine=pd_engine)
send_pd_sql(merged_test8, "player_data", fbref_engine)
