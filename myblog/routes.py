from flask import Flask
import flask_restful as restful
import os
import sys
#from templates.template_route import index
#from templates.template_route import index_

#reload(sys)
#sys.setdefaultencoding("utf-8")


def create_app():

    app = Flask(__name__)
    api = restful.Api(app)
    #app.register_blueprint(index, url_prefix="/blog")
    #app.register_blueprint(index_, url_prefix="/")

    def list_dir(dir):
        child_dir_list = []
        for child_dir in os.listdir(dir):
            if os.path.isdir(dir+"/"+child_dir+"/"):
                child_dir_list.append(child_dir)
        return child_dir_list

    f = open('app.txt', 'r')
    app_list = []
    for line in f:
        app_list.append(line.strip('\n'))

    for appname in app_list:
        for package in list_dir(appname+"/api/"):
            for i in os.listdir(appname+"/api/"+package):
                if os.path.splitext(i)[1] == ".py" and os.path.splitext(i)[0] != "__init__":
                    urlpath = "/api/"+appname+"/"+package+"/"+os.path.splitext(i)[0]

                    fromName = "%s.%s.%s.%s" % (appname, "api", os.path.splitext(package)[0], os.path.splitext(i)[0])
                    tmpModule = __import__(fromName, globals(), locals(), 'Api')

                    api.add_resource(tmpModule.Api, urlpath, endpoint=urlpath)
    return app
