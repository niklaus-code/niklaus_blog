# coding=utf8
from modules.db_conn import DB


class Blog(object):
    def __init__(self):
        self.db = DB()

    def get_blog(self):
        sql = '''
            SELECT t.category_id,t1.category_name, count(t1.category_id) as count
            FROM article_class t
            left join myblog_caegory_info t1 on t.category_id = t1.category_id
            where t.category_id != 6 group by t.category_id ;'''
        res = self.db.query(sql)

        return res
