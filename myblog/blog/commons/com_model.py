# coding=utf8
from datetime import datetime, timedelta
from .token_model import Token
from modules.db_conn import DB


class Blog(object):

    def __init__(self):
        self.time = datetime.now()
        self.db = DB()

    def point_like(self, article_id):
        '''点赞'''
        try:
            sql = '''update myblog_list set like_number=like_number+1 WHERE id=%d''' % article_id
            self.db.insert(sql)
        except:
            return False
        like_number = self.get_like_number(article_id)
        return like_number
        
    def get_like_number(self, article_id):
        sql = '''select like_number from myblog_list where id= %d''' % article_id
        res = self.db.query(sql)
        for like_number in res:
            return like_number[0]
        return False

    def expire_time(self):
        '''返回过期时间'''
        expire_time = self.time + timedelta(days=30)
        return expire_time


    def top_list(self, article_id):
        now_5 = self.expire_time()
        try:
            sql = '''insert into top_list(article_id, expire_time) values (%d, "%s")'''  %(article_id, now_5)
            self.db.insert(sql)
            return True
        except:
            return False

    def get_top_article_id(self):
        sql = '''select article_id from top_list where expire_time > "%s" and status=1''' % self.time
        res = self.db.query(sql)

        topid_list = []
        for topid in res:
            topid_list.append(topid[0])
        return topid_list

    def get_total_number(self, offset):
        sql = '''select count(*)
            from myblog_list m
            where 
            m.id not in (select article_id from article_class 
            where category_id in (5)) and 
            m.status = 1
            '''
        res = self.db.query(sql)
        if res[0][0]%offset > 0:
            return res[0][0]//offset+1
        return res[0][0]//offset

    def get_blog(self, start, offset):
        '''获取所有blog'''
        sql = '''
            select m.id,m.title,m.content, m.img, group_concat(i.category_name)
            from myblog_list m LEFT JOIN article_class a on m.id = a.article_id  LEFT JOIN 
            myblog_caegory_info i
            on a.category_id = i.category_id
            where 
            m.id not in (select article_id from article_class 
            where category_id in (5)) and 
            m.status = 1
            GROUP BY m.id
            order by m.id desc
            limit %d, %d
            ''' % (start, offset)
        res = self.db.query(sql)
        if len(res) > 0:
            return res
        else:
            return False

    def get_top_blog_by_id(self, id=[]):
        id_str = ','.join(str(x) for x in id)
        sql = '''
            select id,title,content,author,substr(create_time,1,19)
            from myblog_list
            where id in (%s)
            ''' % id_str
        res = self.db.query(sql)
        return res

    def get_blog_category(self, category):
        sql = '''
            SELECT id,title,content,author,create_time,like_number
            from myblog_list WHERE id in (
            SELECT article_id FROM article_class WHERE category_id=%d)
            and status = 1
            order by id desc
            ''' % category

        res = self.db.query(sql)

        if len(res) > 0:
            return res
        else:
            return False


    def get_blog_title_id(self):

        sql = '''select id,title from myblog_list'''
        res = self.db.query(sql)

        if len(res) > 0:
            return res
        else:
            return False


    def get_blog_info_by_id(self, id=1212, category=None):
        token = Token()
        # 公共方法传入id调此id的所有所有相关信息
        sql = '''
            select t1.id,
                t1.title,
                t1.content,
                LEFT(t1.create_time,19) as c_time,
                t3.category_name
            from myblog_list t1
            LEFT JOIN article_class t2 ON t2.article_id=%d
            LEFT JOIN myblog_caegory_info t3 ON t2.category_id=t3.category_id
            WHERE t1.id=%d
            ''' % (id, id)
        if category == "read":
            sql = '''SELECT id, title, content, LEFT(create_time, 19) as c_time, "read" as "category" FROM `myblog_read` WHERE status=1 and id =%d''' %id
        res = self.db.query(sql)

        dict_info = {}
        for item in res:
            dict_info["id"] = item[0]
            dict_info["title"] = item[1]
            dict_info["content"] = item[2]
            dict_info["create_time"] = item[3]
            dict_info["category"] = item[4]
            dict_info["signature"] = token.md5_method(token.b64(res[0][0]))
        return dict_info

    def get_article_category(self, articleid):
        sql = '''select * from article_class where article_id=%d ''' % articleid
        res = self.db.query(sql)

        if res:
            return res
        else:
            return False

    def get_all_article_read(self):
        sql = '''select id, title, beginning, author, image from myblog_read where status=1 order by create_time desc'''
        res = self.db.query(sql)

        data = []
        for article in res:
            article_dict = {}
            article_dict["id"] = article[0]
            article_dict["title"] = article[1]
            article_dict["beginning"] = article[2]
            article_dict["author"] = article[3]
            article_dict["image"] = article[4]
            data.append(article_dict)
        return data
