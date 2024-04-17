import os
import pymysql
import pandas as pd
import csv

def getdata_from_db(s, e):
    # Server connection 
    conn = pymysql.connect( 
        host='localhost',
        user='root',
        password='1436',
        db='samsung',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        # Create cursor
        with conn.cursor() as cursor:

            # Execute record select query
            select_query = f"select * from samsung.testDB where Date between '{s}' and '{e}'"
            #select_query = 'select * from samsung.20231219'
            cursor.execute(select_query)
            result = cursor.fetchall() # list

            # Result -> DataFrame
            df = pd.DataFrame(result)
            # Print DataFrame
            #print(df)
            df.to_csv('data_from_db.csv', index=False)
    finally:
        # Close connection
        conn.close()

    return result # df에서 -> result로 수정함

def insert_data():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='1436', 
                           db='samsung', charset='utf8')
    curs = conn.cursor()
    conn.commit()
    
    #####
    files_Path = 'C:\\Users\\leesc\\PycharmProjects\\Mlops-api-server\\collect_files\\' # 파일들이 들어있는 폴더
    file_name_and_time_lst = []
    # 해당 경로에 있는 파일들의 생성시간을 함께 리스트로 넣어줌. 
    for f_name in os.listdir(f"{files_Path}"):
        written_time = os.path.getctime(f"{files_Path}{f_name}")
        file_name_and_time_lst.append((f_name, written_time))
    # 생성시간 역순으로 정렬하고, 
    sorted_file_lst = sorted(file_name_and_time_lst, key=lambda x: x[1], reverse=True)
    # 가장 앞에 이는 놈을 넣어준다.
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
    folder_path = r'C:\\Users\\leesc\\PycharmProjects\\Mlops-api-server\\collect_files\\'
    f = open(folder_path + recent_file_name)
    csvReader = csv.reader(f)

    # DB col : Date, Open, High, Low, Close, Adj Close, Volume
    for row in csvReader: # 1행에 column명이 없는 raw 데이터 형태여야함
        Date = (row[0])
        Open = (row[1])
        High = (row[2])
        Low = (row[3])
        Close = (row[4])
        AdjClose = (row[5])
        Volume = (row[6])
        sql = "insert into samsung.testDB2 (Date, Open, High, Low, Close, AdjClose, Volume) values (%s, %s, %s, %s, %s, %s, %s)"
        val = (Date, Open, High, Low, Close, AdjClose, Volume)
        curs.execute(sql, val)
    conn.commit()
    f.close()
    conn.close()