# coding=utf8
import pymysql
from config import config


class DB(object):

    def __init__(self):
        self.db_host = config.db_conn["DATABASE_URI"]
        self.db_name = config.db_conn["DATABASE_NAME"]
        self.db_port = config.db_conn["DATABASE_PORT"]
        self.db_user = config.db_conn["DATABASE_USER"]
        self.db_passwd = config.db_conn["DATABASE_passwd"]
        self.db = pymysql.connect(db=self.db_name, host=self.db_host, user=self.db_user, passwd=self.db_passwd, charset="utf8")

    def query(self, sql):
        cur = self.db.cursor()
        try:
            cur.execute(sql)
            return cur.fetchall()
        except:
            return False
        finally:
            cur.close()

    def insert(self, sql):
        cur = self.db.cursor()
        try:
            cur.execute(sql)
            conn.commit()
            return True
        except:
            return False
        finally:
            cur.close()
