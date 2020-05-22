# coding =utf8
from datetime import datetime, timedelta
from modules.db_conn import DB


class Login(object):
    def __init__(self):
        self.time = datetime.now()
        self.db = DB()

    def user_login(self, email, passwd, time):
        sql = '''
            select email,random_number from login_record
            where email="%s" and random_number=%d and expire_time > "%s"
            ''' % (email, passwd, time)
        res = self.db.query(sql)

        if res:
            return True
        else:
            return False

    def login_record(self, email, random_number):

        exp = datetime.now()+timedelta(minutes=5)
        sql = '''
            insert into login_record (email,random_number, expire_time)
            values ("%s","%s","%s")
            ''' % (MySQLdb.escape_string(email), random_number, exp)

        try:
            self.db.insert(sql)
            return True
        except:
            return False
