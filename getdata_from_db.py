import os
import pymysql
import pandas as pd
import csv
from datetime import datetime

# DB 연결 및 csv 파일 데이터프레임으로 반환
def getdata_from_db(s, e):
    # Server connection 
    conn = pymysql.connect( 
        host='localhost',
        user='root',
        password='cloud9921!',
        db='samsung',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        
        # cursor 생성
        with conn.cursor() as cursor:

            # select 쿼리
            select_query = f"select * from samsung.20240423_test where Date between '{s}' and '{e}'"
            cursor.execute(select_query)
            result = cursor.fetchall() # list

            # Result -> DataFrame으로 반환
            df = pd.DataFrame(result)
            now = datetime.now().strftime("%Y_%m%d_%H%M%S")
            df.to_csv(f"db_to_df/df_to_db_{now}.csv", index=False)

    finally:
        conn.close()

    return result

# 데이터 삽입
def insert_data():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='cloud9921!', 
                           db='samsung', charset='utf8')
    curs = conn.cursor()
    conn.commit()
    
    files_Path = 'C:/sinheechan.github.io-master/Project_MLops/collect_files/' # 파일들이 들어있는 폴더
    file_name_and_time_lst = []
    
    # 해당 경로에 있는 파일들의 생성시간을 함께 리스트로 넣어줌.
    for f_name in os.listdir(f"{files_Path}"):
        written_time = os.path.getctime(f"{files_Path}{f_name}")
        file_name_and_time_lst.append((f_name, written_time))
    
    # 생성시간 역순으로 정렬하고, 
    sorted_file_lst = sorted(file_name_and_time_lst, key=lambda x: x[1], reverse=True)
    
    # 가장 앞에 파일을 넣어준다.
    recent_file = sorted_file_lst[0]
    recent_file_name = recent_file[0]
    path = str(os.path.abspath(recent_file_name))
    ##### 
    '''
    new_path = []
    for i, s in enumerate(path):
        new_path.append(s)
        if s == "'\'":
            s[i+1].append["'\'"]
    #new_path = str(new_path)
    #print(new_path, type(new_path)) # list
    last_path = ''.join([x if x != '\\' else '\\\\' for x in new_path])
    last_path = str(last_path)
    print(last_path)
    # 'C:\\Users\\leesc\\PycharmProjects\\Mlops-api-server\collect_files\\data_from_db.csv'
    '''
    folder_path = r'C:/sinheechan.github.io-master/Project_MLops/collect_files/'
    f = open(folder_path + recent_file_name)
    csvReader = csv.reader(f)

    # DB 내장된 column : Date, Open, High, Low, Close, Adj Close, Volume
    for row in csvReader: # 1행에 column명이 없는 raw 데이터 형태여야함
        Date = (row[0])
        Open = (row[1])
        High = (row[2])
        Low = (row[3])
        Close = (row[4])
        AdjClose = (row[5])
        Volume = (row[6])
        sql = "insert into samsung.20240423_test (`Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, `Volume`) values (%s, %s, %s, %s, %s, %s, %s)"
        val = (Date, Open, High, Low, Close, AdjClose, Volume)
        curs.execute(sql, val)

        
    conn.commit()
    f.close()
    conn.close()

print('Insert 가 완료되었습니다')