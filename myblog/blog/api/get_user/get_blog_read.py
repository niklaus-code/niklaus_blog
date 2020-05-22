# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import com_model
from ...commons import token_model


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.args = self.get_args.parse_args()

    def get(self):
        is_token = token_model.Token()
        obj_blog = com_model.Blog()
        readblogs = obj_blog.get_all_article_read()

        return readblogs

