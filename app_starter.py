# 서버 구동하는 파일

from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import os
import data_from_yf
from project.test import maria_test
import getdata_from_db
from datetime import datetime

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app, version='1.0', title='API 문서 생성', description='개발하면서 문서 동시 작업 to swagger')

    test_api = api.namespace('test', description='Test API를 위한 사이트입니다.') # test
    
    data = api.namespace('getdata', description='데이터 get API') # use1
    data_from_db = api.namespace('getdatafromdb', description='DB로부터 data Get_API') # use2

    @test_api.route('/') 
    class Test(Resource):
        def get(self):
            return "Test를 위한 서버입니다."
    
    @data.route('/')
    class GetData(Resource):
        def get(self):
            s = request.args.get('s', default='2024-01-01',type=str)
            e = request.args.get('e', default='2024-12-31',type=str) 
            stocks = request.args.get('stocks', type = str) 
            
            print(s, e, type(s))

            start_date = datetime.strptime(s, '%Y-%m-%d')
            end_date = datetime.strptime(e, '%Y-%m-%d')

            print(start_date, end_date, type(start_date))
            return data_from_yf.getdata(start_date, end_date, stocks)
        
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
  
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 9999)), debug=True)