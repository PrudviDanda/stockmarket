import os
import csv
import pandas as pd
from sqlalchemy import create_engine, types

MYSQL_USER='root'
MYSQL_PASS='P@rtyb00th'
MYSQL_HOST='localhost'
MYSQL_DB_NAME = 'stock_master'
MYSQL_TB_NAME = 'stocks'
basepath_stocks = r'C:\Users\Prudvi\Downloads\Stock-Market\Stocks'

mysql_import=r'C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe'

""" engine = create_engine('mysql://{0}:{1}@{2}/{3}'.format(MYSQL_USER,MYSQL_PASS,MYSQL_HOST,MYSQL_DB_NAME))

with os.scandir(basepath_stocks) as entries:
    count =1
    for entry in entries:
        if count < 2:
            print(entry.path)
            df = pd.read_csv(entry.path,sep=',',quotechar='\'',encoding='utf8')
            df.to_sql(MYSQL_TB_NAME,con=engine,index=False,if_exists='append')
        else :
            break
        count = count+1       """

with os.scandir(basepath_stocks) as entries:
    count =0
    for entry in entries:
        if count < 1:
            print(entry.path)
            print(entry.path.replace('\\','/'))
            b=entry.path.replace('/','\\')
            print("cmd /c \'{0}\' -u{1} -p{2}  --local-infile {5} -e \" LOAD DATA LOCAL INFILE {3} INTO TABLE {4} FIELDS TERMINATED BY \',\' LINES TERMINATED BY \'\\n\' \"".format(mysql_import,MYSQL_USER,MYSQL_PASS,b,MYSQL_TB_NAME,MYSQL_DB_NAME))
            os.system("cmd /c \'{0}\' -u{1} -p{2}  --local-infile {5} -e \" LOAD DATA LOCAL INFILE {3} INTO TABLE {4} FIELDS TERMINATED BY \',\' LINES TERMINATED BY \'\\n\' \"".format(mysql_import,MYSQL_USER,MYSQL_PASS,entry.path,MYSQL_TB_NAME,MYSQL_DB_NAME))
            #os.system("cmd /c \"{0}\" --db {1} --collection {2} --type csv --headerline --file {3} --numInsertionWorkers 5".format(mongo_import,MDB_DB_NAME,MDB_COL_NAME,entry.path))
        else :
            break
        count = count+1