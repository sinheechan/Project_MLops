# 서버 구동하는 파일

from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import os
import data_from_yf
from project.test import maria_test
import getdata_from_db

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
            s = request.args.get('s',1,str) # 시작날짜
            e = request.args.get('e',1,str) # 끝날짜
            print(s, e, type(s))
            return data_from_yf.getdata(s, e) # 시작, 끝날짜 가지고 함수 호출 => data_from_yf.py
        
    @data_from_db.route('/')
    class GetDataFromDB(Resource):
        def get(self):
            s = request.args.get('s',1,str)
            e = request.args.get('e',1,str)
            print(s, e, type(s))
            return getdata_from_db.getdata_from_db(s, e)
        
    @external_data_col.route('/')
    class ExternalDataCollection(Resource):
        def get(self):
            s = request.args.get('s',1,str)
            e = request.args.get('e',1,str)
            print(s, e, type(s))
            return data_from_yf.getdata(s, e)
            
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 9999)), debug=True)