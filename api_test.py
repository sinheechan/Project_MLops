import requests
from datetime import datetime
import pandas as pd
import json

url = 'http://127.0.0.1:9999/getdata'
param = {'s': '2017-01-01', 'e': '2022-12-31'} # parameter로 시작날짜, 종료날짜 전달
res = requests.get(url, params=param)
recv_data = res.text
recv_data_to_json = json.loads(recv_data) # str -> json
print(type(recv_data_to_json))
df = pd.read_json(recv_data_to_json) # json -> dataframe
print(df)