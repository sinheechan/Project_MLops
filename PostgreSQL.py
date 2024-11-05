import pandas as pd
from sqlalchemy import create_engine

# DBeaver에서 불러온 주식 데이터를 DataFrame으로 변환
df = pd.DataFrame(주식_데이터)

# PostgreSQL 연결 설정
engine = create_engine("postgresql://username:password@host:port/dbname")

# DataFrame을 PostgreSQL 테이블로 전송
df.to_sql('table_name', engine, if_exists='replace', index=False)