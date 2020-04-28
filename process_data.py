import os
import pandas as pd

# basepath_stocks = r'C:\Users\Prudvi\Downloads\stock-market-dataset\stocks'
basepath_stocks = r'/mnt/c/Users/Prudvi/Downloads/stock-market-dataset/etfs'
# new_basepath_stocks = r"C:\Users\Prudvi\Downloads\Stock-Market\Stocks"
new_basepath_stocks = r'/mnt/c/Users/Prudvi/Downloads/Stock-Market/Etfs'

with os.scandir(basepath_stocks) as entries:
    count =0
    for entry in entries:
        print(entry.path)
        df = pd.read_csv(entry.path)
        # Add a New Column with name: Symbol and populate it with filename as data 
        df["Symbol"] = entry.name[:-4]
        # Reorder the headers for cleaner look 
        df = df[["Symbol", "Date", "Adj Close", "Open", "High", "Low", "Close", "Volume"]]
        # Save new CSV 
        df.to_csv(os.path.join(new_basepath_stocks, entry.name), index=False)
        
