# coding=utf8
from .token_model import Token
from modules.db_conn import DB


class Blog(object):
    def __init__(self):
        self.db = DB()

    def get_blog(self, date):
        token = Token()
        sql = '''SELECT * FROM myblog_list t WHERE create_time like "%s%%";''' % date[0]

        res = self.db.query(sql)

        list = []
        for i in res:
            dict = {}
            dict["id"] = i[0]
            dict["title"] = i[1]
            dict["content"] = i[2]
            dict["like"] = i[3]
            dict["author"] = i[4]
            dict["create_time"] = str(i[5])
            dict["signature"] = token.md5_method(token.b64(i[0]))
            list.append(dict)
        return list

    def count_date(self):
        sql = '''SELECT SUBSTR(create_time, 1, 7), count(id) FROM myblog_list t GROUP BY DATE_FORMAT(create_time, '%y-%m')'''
        res = self.db.query(sql)
        date_list = []
        for one in res:
            date_dict = {}
            date_dict["date"] = one[0]
            date_dict["number"] = one[1]
            date_dict["info"] = self.get_blog(one)
            date_list.append(date_dict)
        return date_list
