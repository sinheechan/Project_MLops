import sys
sys.path.append('.')
from sqlalchemy import text
from project.common.maria_data_service import MariaDataService
from project.constants.default_constants import DefaultConstants
from project.db.test_sql import TestSql
import app_starter
from flask import jsonify

maria_service = MariaDataService.instance()

def getdata_from_db(s, e):
    #test = maria_service.get(text(TestSql.SQL_GET_TEST))
    sql = f"select * from samsung.20231216 where Date between '{s}' and '{e}'"
    print(sql, type(sql))
    #test2 = maria_service.get(text("select * from samsung.20231216"))
    test3 = maria_service.get(text(sql))
    #print(len(test), test)
    #print(len(test2), test2[0])
    #print(test2, type(test2))
    print(len(test3), test3[0], type(test3))
    return str(test3) # list -> json
#getdata_from_db('2023-01-01', '2023-12-31')