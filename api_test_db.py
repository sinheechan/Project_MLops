# getting data TEST from DB
import requests
from datetime import datetime
import pandas as pd
from flask import jsonify
import json

def DBtest():
    url = 'http://127.0.0.1:9999/getdatafromdb'
    param = {'s': '2023-01-01', 'e': '2024-12-31'}
    res = requests.get(url, params=param)
    print(res)
    recv_data_from_db = res.content

if __name__ == '__main__':
    url = 'http://127.0.0.1:9999/getdatafromdb'
    param = {'s': '2023-01-01', 'e': '2024-12-31'}
    res = requests.get(url, params=param)
    recv_data = res.text
    print(recv_data, type(recv_data))