# dbeaver 연결

# Use pymysql
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# localhost = 내 ip
conn = pymysql.connect(host='localhost', user='root', password='cloud9921!' ,
                       db='samsung', charset='utf8')
query = 'select * from samsung.20240423_test' # SQL 쿼리문 # DB명 테이블몇 Check
df = pd.read_sql_query(query,conn) # Pandas 호출 및 DB 적재
print(df)

'''
pymysql.install_as_MySQLdb()
engine = create_engine("mysql://user:password@host/db")
df.to_sql(name='new_perfomance_log', con=engine, if_exists='append', index=False)
                                     # if_exists='append' : table 존재시 데이터만 추가
                                     # index=False : index 값 넣지 않기
'''