# Getdata 클래스에 탑재되어 파일의 형태 변환 및 저장을 담당한다.

from datetime import datetime
import pandas as pd
from pandas_datareader import data as pdr
import pickle
import json
import yfinance as yf
from flask import jsonify
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
    filename = datetime.now().strftime("%Y%m%d_%H%m%S")
    df = pdr.get_data_yahoo(stocks, s, e)
    df_to_json = df.to_json()
    with open('temp.csv', 'w') as f:
        f.write(df_to_json)

    # 데이터 저장
    now = datetime.now().strftime("%Y_%m%d_%H%M%S")
    filename = f"collect_files/df_{now}.csv"
    df.to_csv(filename, index=True, header=False)
        
    return jsonify(df_to_json)




