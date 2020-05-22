#!/env/python
# coding=utf-8
import routes
import os

'''
pro：生产环境配置
test：测试环境配置
'''

os.environ["env"] = "pro"
app = routes.create_app()


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
