# dbeaver 연결

# Use pymysql
import pandas as pd
import pymysql
from sqlalchemy import create_engine

# localhost = 내 ip
conn = pymysql.connect(host='localhost', user='root', password='' ,
                       db='samsung', charset='utf8')
query = 'select * from samsung.20231216' # SQL 쿼리문 
df = pd.read_sql_query(query,conn) # pandas에서 호출해서 db에 담는 부분
print(df)

'''
pymysql.install_as_MySQLdb()
engine = create_engine("mysql://user:password@host/db")
df.to_sql(name='new_perfomance_log', con=engine, if_exists='append', index=False)
                                     # if_exists='append' : table 존재시 데이터만 추가
                                     # index=False : index 값 넣지 않기
'''