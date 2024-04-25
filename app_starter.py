# 서버 구동하는 파일

from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import os
import data_from_yf
from project.test import maria_test # db 연결하는 모듈
import getdata_from_db # getdata_from_db.py
from datetime import datetime

if __name__ == '__main__': #  직접 실행될 때 구동
    app = Flask(__name__) # Flask 애플리케이션을 생성
    api = Api(app, version='1.0', title='API 문서 생성', description='개발하면서 문서 동시 작업', doc='/api-docs') # Flask-RESTx를 사용하여 Flask 애플리케이션에 API를 추가

    # api 네임스페이스 생성
    test_api = api.namespace('test', description='Test API를 위한 사이트입니다.') # 함수 경로, 
    data = api.namespace('getdata', description='데이터 get API') 
    data_from_db = api.namespace('getdatafromdb', description='Getiing data from DB API')
    external_data_col = api.namespace('extdatacol', description='External data collection API')

    # API 네임스페이스를 정의하고 해당 엔드포인트에 대한 요청을 처리
    # 외부 데이터를 CSV파일로 받아오고 DB에 적재하는 과정
    

    # api_test.py => 단순자료 반환
    @test_api.route('/') 
    class Test(Resource):
        def get(self):
            return "Test를 위한 서버입니다."
    
    # GetData - (postman) - data_from_yf - watcher - getdata_from_db.py
    @data.route('/')
    class GetData(Resource):
        def get(self):
            s = request.args.get('s', default='2024-01-01',type=str) # 시작일자
            e = request.args.get('e', default='2024-12-31',type=str) # 마감일자
            stocks = request.args.get('stocks', type = str) # 요청자료 코드
            
            print(s, e, type(s))

            start_date = datetime.strptime(s, '%Y-%m-%d') # 시작날짜 문자열 Datetime 변환
            end_date = datetime.strptime(e, '%Y-%m-%d') # 마감날짜 문자열 Datetime 변환

            print(start_date, end_date, type(start_date))
            return data_from_yf.getdata(start_date, end_date, stocks)
        
    
    # getdata_from_db.py / 볼러온 데이터 DF로 변환
    @data_from_db.route('/')
    class GetDataFromDB(Resource):
        def get(self):
            s = request.args.get('s', default='2024-01-01',type=str)
            e = request.args.get('e', default='2024-12-31',type=str)
            
            print(s, e, type(s))

            start_date = datetime.strptime(s, '%Y-%m-%d')
            end_date = datetime.strptime(e, '%Y-%m-%d')

            print(start_date, end_date, type(start_date))
            
            return getdata_from_db.getdata_from_db(start_date, end_date)
    
    # external_api_test.py => 외부데이터 수집
    @external_data_col.route('/')
    class ExternalDataCollection(Resource):
        def get(self):
            s = request.args.get('s', default='2024-01-01',type=str)
            e = request.args.get('e', default='2024-12-31',type=str)
            
            print(s, e, type(s))
            
            start_date = datetime.strptime(s, '%Y-%m-%d')
            end_date = datetime.strptime(e, '%Y-%m-%d')

            print(start_date, end_date, type(start_date))
            
            return data_from_yf.getdata(start_date, end_date)
            
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 9999)), debug=True)