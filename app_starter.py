# 서버 구동하는 파일

from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import os
import data_from_yf
from project.test import maria_test # db 연결하는 모듈
import getdata_from_db # getdata_from_db.py
from datetime import datetime

if __name__ == '__main__': #  직접 실행
    app = Flask(__name__)
    api = Api(app, version='1.0', title='API 문서 생성', description='개발하면서 문서 동시 작업 to swagger')

    # test
    test_api = api.namespace('test', description='Test API를 위한 사이트입니다.')
    
    # use
    data = api.namespace('getdata', description='데이터 get API') 
    data_from_db = api.namespace('getdatafromdb', description='DB로부터 data Get_API')
    external_data_col = api.namespace('extdatacol', description='외부데이터 수집_API')

    # api_test.py => 단순자료 반환
    @test_api.route('/') 
    class Test(Resource):
        def get(self):
            return "Test를 위한 서버입니다."
    
    # GetData - stocks(postman) - data_from_yf - watcher - getdata_from_db.py
    @data.route('/')
    class GetData(Resource):
        def get(self):
            s = request.args.get('s', default='2024-01-01',type=str) # 시작일자
            e = request.args.get('e', default='2024-12-31',type=str) # 마감일자
            stocks = request.args.get('stocks', type = str) 
            
            print(s, e, type(s))

            start_date = datetime.strptime(s, '%Y-%m-%d')
            end_date = datetime.strptime(e, '%Y-%m-%d')

            print(start_date, end_date, type(start_date))
            return data_from_yf.getdata(start_date, end_date, stocks)
        
    
    # getdata_from_db.py / 볼러온 데이터 DF로 변환 / DBeaver 적재
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
    
    # external_api_test.py => 외부데이터 수집 (단순날짜)
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