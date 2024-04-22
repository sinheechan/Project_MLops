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
    api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc='/api-docs')

    test_api = api.namespace('test', description='Test API') # 콜 받는 주소
    data = api.namespace('getdata', description='데이터 get API')
    data_from_db = api.namespace('getdatafromdb', description='Getiing data from DB API')
    external_data_col = api.namespace('extdatacol', description='External data collection API')

    @test_api.route('/')
    class Test(Resource):
        def get(self):
            return "Hello World. This is Test."
    
    @data.route('/')
    class GetData(Resource):
        def get(self):
            s = request.args.get('s', default='2024-01-01',type=str)
            e = request.args.get('e', default='2024-12-31',type=str)
            print(s, e, type(s))
                    # Convert string to datetime
            start_date = datetime.strptime(s, '%Y-%m-%d')
            end_date = datetime.strptime(e, '%Y-%m-%d')

            print(start_date, end_date, type(start_date))
            return data_from_yf.getdata(start_date, end_date)
        
    @data_from_db.route('/')
    class GetDataFromDB(Resource):
        def get(self):
            s = request.args.get('s', default='2024-01-01',type=str)
            e = request.args.get('e', default='2024-12-31',type=str)
            print(s, e, type(s))
            # Convert string to datetime
            start_date = datetime.strptime(s, '%Y-%m-%d')
            end_date = datetime.strptime(e, '%Y-%m-%d')

            print(start_date, end_date, type(start_date))
            return getdata_from_db.getdata_from_db(start_date, end_date)
        
    @external_data_col.route('/')
    class ExternalDataCollection(Resource):
        def get(self):
            s = request.args.get('s', default='2024-01-01',type=str)
            e = request.args.get('e', default='2024-12-31',type=str)
            print(s, e, type(s))
                    # Convert string to datetime
            start_date = datetime.strptime(s, '%Y-%m-%d')
            end_date = datetime.strptime(e, '%Y-%m-%d')

            print(start_date, end_date, type(start_date))
            return data_from_yf.getdata(start_date, end_date)
            
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 9999)), debug=True)