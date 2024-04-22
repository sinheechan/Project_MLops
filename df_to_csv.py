from pandas_datareader import data as pdr
from datetime import datetime
import pandas as pd
import yfinance as yf
yf.pdr_override()

start = datetime(2017,1,1)
end = datetime(2023,12,31)
filename = datetime.now().strftime("%Y%m%d_%H%m%S")
df = pdr.get_data_yahoo('005930.KS', start, end)
print(df)
#df.to_excel(filename + '_df.xlsx') # If you want to extract excel, use this line 
df.to_csv(filename + '_df.csv')