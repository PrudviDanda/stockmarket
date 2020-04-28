import os
import csv
import pandas as pd
from sqlalchemy import create_engine, types

MYSQL_USER='root'
MYSQL_PASS='Iphone_36'
MYSQL_HOST='localhost'
MYSQL_DB_NAME = 'stockmarket'
MYSQL_TB_NAME = 'etfs'
# basepath_stocks = r'C:\Users\Prudvi\Downloads\Stock-Market\Stocks'
basepath_stocks = r'/mnt/c/Users/Prudvi/Downloads/Stock-Market/Etfs'


engine = create_engine('mysql://{0}:{1}@{2}/{3}'.format(MYSQL_USER,MYSQL_PASS,MYSQL_HOST,MYSQL_DB_NAME))
# df = pd.read_csv(basepath_stocks)
# df.to_sql(MYSQL_TB_NAME,con=engine,index=False,if_exists='append')

with os.scandir(basepath_stocks) as entries:
    count =0
    for entry in entries:
        if count < 1000000000000000:
            print(entry.path)
            df = pd.read_csv(entry.path,sep=',',quotechar='\'',encoding='utf8')
            df.to_sql(MYSQL_TB_NAME,con=engine,index=False,if_exists='append')
        else :
            break
        count = count+1  