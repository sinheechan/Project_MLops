from pandas_datareader import data as pdr
from datetime import datetime
import pandas as pd
import yfinance as yf
import os

yf.pdr_override()

start = datetime(2023, 1, 1)
end = datetime.now()
file_path = 'C:/sinheechan.github.io-master/Project_MLops/collect_files'

filename = datetime.now().strftime("%Y%m%d_%H%m%S")
df = pdr.get_data_yahoo('005930.KS', start, end) #TSLA

# CSV 파일 경로 설정
csv_file_path = os.path.join(file_path, filename + '_df.csv')

# 데이터프레임을 CSV 파일로 저장
df.to_csv(csv_file_path)

print("CSV 파일이 저장되었습니다:")