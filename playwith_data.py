import os
import matplotlib.pyplot as plt
import pandas as pd

basepath = r'C:\Users\Prudvi\Downloads\stock-market-dataset\stocks'

with os.scandir(basepath) as entries:
    count =0
    for entry in entries:
        if count < 1:
            print(entry.path)
            df = pd.read_csv(entry.path)
            print(df.head())
            print(df.shape)
            # plot a histogram  
            #df['Adj Close'].hist(bins=10) 
            
            # shows presence of a lot of outliers/extreme values 
            df.boxplot(column='Adj Close', by = 'Date') 
            
            # plotting points as a scatter plot 
            y = df["Adj Close"] 
            x = df["Date"] 
            plt.scatter(x, y, label= "stars", color= "m",  
                        marker= "*", s=30) 
            # x-axis label 
            plt.xlabel('Adj Close') 
            # frequency label 
            plt.ylabel('Date') 
            # function to show the plot 
            plt.show() 

            # # plot the data itself
            # pylab.plot(x,y,'o')

            # # calc the trendline
            # z = numpy.polyfit(x, y, 1)
            # p = numpy.poly1d(z)
            # pylab.plot(x,p(x),"r--")
            # # the line equation:
            # print "y=%.6fx+(%.6f)"%(z[0],z[1])
        else :
            break
        count = count+1
        
