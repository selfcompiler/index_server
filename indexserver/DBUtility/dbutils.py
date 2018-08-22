__author__ = 'rahul.sk'

import traceback
import logging
import sys
import  os

try:
    import pymysql as commonmysql
except ImportError:
    import MySQLdb as commonmysql

from indexserver.dbconfig.DBConfig import DBConfig


class DBUtils:

    def __init__(self):
        print("DBUtils Object Constructed")

    @staticmethod
    def execute_select_query(keyName,query):
        db = commonmysql.connect(DBConfig.getHost(keyName),DBConfig.getUser(keyName),DBConfig.getPassword(keyName),DBConfig.getDB(keyName))
        cursor = db.cursor()
        cursor.execute(query)
        resultSet=cursor.fetchall();
        db.close()
        return resultSet;

    @staticmethod
    def execute_except_select_query(keyName,query):
        print ("Starting execute_except_select_query")
        try:
            db = commonmysql.connect(DBConfig.getHost(keyName), DBConfig.getUser(keyName), DBConfig.getPassword(keyName),
                             DBConfig.getDB(keyName))
            cursor = db.cursor()
            print ("Execute Query started")
            cursor.execute(query)
            print ("Execute Query completed")
            db.commit()
            db.close()
        except Exception as e:
            #print ("Exception : \n"+e)
            return logging.error(traceback.format_exc())
