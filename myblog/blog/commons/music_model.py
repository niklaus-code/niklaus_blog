# coding =utf8

class Music(object):

    def __init__(self):
        self.db = MySQLdb.connect(db='myblog', host='127.0.0.1', user='ysman', passwd='123456', charset="utf8")
        self.cur_blog = self.db.cursor()

    def get_song_list(self):
        sql = '''
            select song_name,song_url from music
            '''
        self.cur_blog.execute(sql)
        res = self.cur_blog.fetchall()
        return res
