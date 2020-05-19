import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy 
# https://www.dataquest.io/blog/how-to-analyze-survey-data-python-beginner/ 
#basepath = r'/mnt/c/Users/Prudvi/Downloads/Stock-Market/Stocks'
basepath = r'C:\Users\Prudvi\Downloads\stock-market-dataset\stocks'
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
            #df["Adj Close"] =df["Adj Close"].astype(float)
            # print(df.head())
            print("Plotting points as a scatter plot")
            y = df["Adj Close"] 
            x = df["Date"] 
            # x-axis label 
            plt.xlabel('Date') 
            plt.ylabel('Adj Close') 
            plt.scatter(x, y)
            
            # plt.plot(x, y,'o')
            z = numpy.polyfit(x, y, 1)
            p = numpy.poly1d(z)
            plt.plot(x,p(x),"r--")
            #pylab.plot(x,p(x),"r--")
            plt.show() 


        else :
            break
        count = count+1
        
