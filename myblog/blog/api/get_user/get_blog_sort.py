# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import get_blog_by_category


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        # self.get_args.add_argument('category', type=str, required=True, default="python", location='')
        self.args = self.get_args.parse_args()

    def post(self):

        istance = get_blog_by_category.Blog()
        blog = istance.get_blog()

        if blog:
            return {"data": blog}
        else:
            return False
