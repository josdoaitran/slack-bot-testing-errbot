import os

import pymysql.cursors
import string, mysql.connector
from mysql.connector import errorcode

class Mysql_Util:

    def execute_mysql_command_util(dbUrl, userName, password, database, sql_commnand, ssl=None):
        env = os.environ['app_env']
        if env == 'local':
            ssl = None;
        if not ssl:
            connection = pymysql.connect(host=dbUrl,
                                     user=userName,
                                     password=password,
                                     db=database,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        else:
            connection = pymysql.connect(host=dbUrl,
                                         user=userName,
                                         password=password,
                                         db=database,
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor,
                                         ssl={'ca': '/err/local_plugins/rds-ca-2019-root.pem'})
        try:
            with connection.cursor() as cursor:
                print("******** Start execute: " + "********")
                print("******** " + sql_commnand + "********")
                cursor.execute(sql_commnand)
                result = cursor.fetchone()
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print("******** Execution successfully. ********")
        finally:
            connection.close()
        return result

    def query_mysql_command_util(dbUrl, userName, password, database, sql_commnand, ssl = None):
        if not ssl:
            connection = pymysql.connect(host=dbUrl,
                                     user=userName,
                                     password=password,
                                     db=database,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        else:
            connection = pymysql.connect(host=dbUrl,
                                         user=userName,
                                         password=password,
                                         db=database,
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor,
                                         ssl={'ca': '/err/local_plugins/rds-ca-2019-root.pem'})

        try:
            with connection.cursor() as cursor:
                print("******** Start execute: " + "********")
                print("******** " + sql_commnand + "********")
                cursor.execute(sql_commnand)
                result = cursor.fetchone()
            # connection is not autocommit by default. So you must commit to save
            # your changes.
                return result
            print("******** Execution successfully. ********")
        finally:
            connection.close()
        return result

