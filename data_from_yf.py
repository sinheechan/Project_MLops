# 외부데이터 자동 수집 후 JSON으로 반환

from datetime import datetime
import pandas as pd
from pandas_datareader import data as pdr
import pickle
import json
import yfinance as yf
from flask import jsonify
import os
yf.pdr_override()

def getdata(s, e, stocks):
    dic = dict()
    '''
    y = s[0:4]
    m = s[5:7]
    d = s[8:]
    y1 = e[0:4]
    m1 = e[5:7]
    d1 = e[8:]    
    start = datetime(int(y),int(m),int(d))
    end = datetime(int(y1),int(m1),int(d1))
    filename = datetime.now().strftime("%Y%m%d_%H%m%S")
    df = pdr.get_data_yahoo('005930.KS', start, end)
    #pic = pd.to_pickle(df, filename + '.pickle')
    print(type(df))
    '''
    filename = datetime.now().strftime("%Y%m%d_%H%M%S")
    df = pdr.get_data_yahoo(stocks, s, e) # TSLA / 005930.KS(삼성) to Postman
    df_to_json = df.to_json()
    
    file_path = os.path.join('C:/sinheechan.github.io-master/Project_MLops/collect_files', filename)
    with open(file_path, 'w') as f:
        f.write(df_to_json)
        
    return jsonify(df_to_json)