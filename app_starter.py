# 서버 구동하는 파일

from flask import Flask, request
from flask_restx import Api, Resource, reqparse
import os
import data_from_yf
from project.test import maria_test
import getdata_from_db
from datetime import datetime

if __name__ == '__main__': #  현재 스크립트가 직접 실행될 때만 아래의 코드 블록을 실행
    app = Flask(__name__) # Flask 애플리케이션을 생성
    api = Api(app, version='1.0', title='API 문서', description='Swagger 문서', doc='/api-docs') # Flask-RESTx를 사용하여 Flask 애플리케이션에 API를 추가

    test_api = api.namespace('test', description='Test API') # 각 네임스페이스 별 설명 포함
    data = api.namespace('getdata', description='데이터 get API') 
    data_from_db = api.namespace('getdatafromdb', description='Getiing data from DB API')
    external_data_col = api.namespace('extdatacol', description='External data collection API')

    # API 네임스페이스를 정의하고 해당 엔드포인트에 대한 요청을 처리
    # 각 네임스페이스는 특정 기능을 수행하고 해당하는 데이터를 반환
    
    @test_api.route('/') # api_test.py => 단순 결과 자료 반환
    class Test(Resource):
        def get(self):
            return "Hello World. This is Test."
    
    @data.route('/') # getdata_test.py => 커밋 필요
    class GetData(Resource):
        def get(self):
            s = request.args.get('s', default='2024-01-01',type=str)
            e = request.args.get('e', default='2024-12-31',type=str)
            print(s, e, type(s))
                    # Convert string to datetime
            start_date = datetime.strptime(s, '%Y-%m-%d')
            end_date = datetime.strptime(e, '%Y-%m-%d')

            print(start_date, end_date, type(start_date))
            return data_from_yf.getdata(start_date, end_date) # get 데이터에서 전달할 인자 수정
        

    @data_from_db.route('/') # getdata_from_db.py
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
        
    @external_data_col.route('/') # external_api_test.py
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