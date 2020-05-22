# coding =utf8
from datetime import datetime, timedelta
from modules.db_conn import DB


class UsPrama(object):
    def __init__(self):
        self.time = datetime.now()
        self.db = DB()

    def prama(self):
        sql = '''
            SELECT id,title  FROM `us_prama`;
            '''
        res = self.db.query(sql)
        plotlist = []
        for plot in res:
            plotdict = {}
            plotdict["id"] = plot[0]
            plotdict["title"] = plot[1]
            plotlist.append(plotdict)
        return plotlist    
