import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy 
# https://www.dataquest.io/blog/how-to-analyze-survey-data-python-beginner/ 
basepath = r'/mnt/c/Users/Prudvi/Downloads/Stock-Market/Stocks'
start_date="2018-01-01"
end_date = "2020-01-30"

with os.scandir(basepath) as entries:
    count =0
    for entry in entries:
        if count < 1:
            print(entry.path)
            df = pd.read_csv(entry.path)
            df = df[["Date", "Adj Close"]]
            df = df.loc[(df['Date'] > start_date) & (df['Date'] <= end_date)]
            print(df.head())
            print(df.shape)
            df.boxplot(column='Adj Close', by = 'Date') 

        else :
            break
        count = count+1
        
