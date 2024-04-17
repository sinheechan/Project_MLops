import sys
sys.path.append('.')
from sqlalchemy.orm import scoped_session, sessionmaker
from project.common.single_instance import SingletonInstance
from sqlalchemy import create_engine
from project.constants.default_constants import DefaultConstants
import pandas as pd


class MariaDataService(SingletonInstance):
    #생성자
    def __init__(self):
        # 개발
        '''
        self.engine = create_engine('postgresql://postgres:kepco123456/@100.216.222.101:31067/postgres',
                                pool_recycle=100,
                                pool_size=300,
                                max_overflow = 50,
                                echo=None                                )
        '''
        # 운영
        self.engine = create_engine('mysql://root:1436@localhost:3306/samsung',
                                    pool_recycle=100,
                                    pool_size=500,
                                    max_overflow=100,
                                    echo=None)
        self.Session = scoped_session(sessionmaker(autoflush=True, bind=self.engine))

    #데이터 조회
    def get(self,sql):
        session = self.Session()
        result_list = session.execute(sql)
        result_list = result_list.fetchall()
        session.close()
        return result_list
    #end def get(self,sql,param_dict):

    #데이터 입력,수정,삭제
    def execute(self,sql):
        session = self.Session()
        session.execute(sql)
        session.close()
    #end def get(self,sql,param_dict):

    #데이터 변환(tuple -> dict)
    def transform_dict(self, param_list):
        result_list = list()
        for param in param_list:
            result_list.append(dict(param))
        #end for param in param_list:
        return result_list
    #end def transform_dict(self, param_list):