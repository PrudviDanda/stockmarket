import yfinance as yf
from pandas_datareader import data as pdr
#yf.pdr_override() 

#data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")

# msft = yf.Ticker("MSFT")

# # get stock info
# #print(msft.info)

data = yf.download(tickers = "MSFT",period = "2y",interval = "1wk",group_by = 'ticker')
#data = yf.download("SPY AAPL", start="2017-01-01", end="2017-04-30", group_by="ticker")

print(data["MSFT"]['Close'])