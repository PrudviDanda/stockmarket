import os
import json
from pymongo import MongoClient
import pandas as pd

MDB_DB_NAME = 'Mongo_Stocks'
MDB_COL_NAME = 'Stock_Tickers'
basepath_stocks = r'C:\Users\Prudvi\Downloads\Stock-Market\Stocks'
new_basepath_stocks = r'C:\Users\Prudvi\Downloads\Stock-Market\Stocks_Json'
mongo_import=r'C:\Program Files\MongoDB\Server\4.2\bin\mongoimport.exe'

# DB connectivity
""" mdb_client = MongoClient('localhost', 27017)
mdb_db = mdb_client[MDB_DB_NAME] 
db_cm = mdb_db[MDB_COL_NAME]
 """
with os.scandir(basepath_stocks) as entries:
    count =0
    for entry in entries:
        if count < 10000000:
            print(entry.path)
            os.system("cmd /c \"{0}\" --db {1} --collection {2} --type csv --headerline --file {3} --numInsertionWorkers 5".format(mongo_import,MDB_DB_NAME,MDB_COL_NAME,entry.path))
        else :
            break
        count = count+1

"""         
with os.scandir(basepath_stocks) as entries:
    count =0
    for entry in entries:
        if count < 1:
            print(entry.path)
            df = pd.read_csv(entry.path)
            df.to_json(os.path.join(new_basepath_stocks, entry.name))
            jdf = open(os.path.join(new_basepath_stocks, entry.name)).read()                        # loading the json file 
            data_json = json.loads(jdf) 
            db_cm.insert_one(data_json) 
            #df = pd.read_csv(entry.path)
        else :
            break
        count = count+1 """
        