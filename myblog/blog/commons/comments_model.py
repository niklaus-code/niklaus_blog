# coding =utf8

class comments(object):

    def __init__(self):
        self.db = MySQLdb.connect(db='myblog', host='127.0.0.1', user='ysman', passwd='123456', charset="utf8")
        self.cur_blog = self.db.cursor()

    def insert_comments(self, comment_content, article_id=0, user_id=0, parent_id=0):
        self.db.autocommit(1)
        sql = ''' 
              insert into comment_list(comment_content,article_id,user_id, parent_id) \
              values ("%s", %d, %d, %d) 
              ''' % (MySQLdb.escape_string(comment_content), article_id, user_id, parent_id)
        self.cur_blog.execute(sql)
        self.db.close()
        return True

    def get_comments(self, article_id):
        self.db.autocommit(1)
        sql = ''' 
                 select comment_content,article_id,user_id,parent_id from comment_list where article_id=%d  order by id desc 
              ''' % article_id
        self.cur_blog.execute(sql)
        res = self.cur_blog.fetchall()
        self.db.close()
        return res
