# dbeaver 연결후 파일 가져오기

import pandas as pd
import pymysql
from sqlalchemy import create_engine

# localhost 정보
conn = pymysql.connect(host='localhost', user='root', password='cloud9921!' ,
                       db='samsung', charset='utf8')

query = 'select * from samsung.20240423_test' # SQL
df = pd.read_sql_query(query,conn) # Pandas 호출 & DB 적재
print(df)