# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import comments_model
from flask import make_response, jsonify
import json


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument('content', type=str)
        self.get_args.add_argument('article_id', type=int)
        self.args = self.get_args.parse_args()

    def post(self):

        istance = comments_model.comments()
        res = istance.get_comments(self.args['article_id'])

        if res:
            return {"data": res}
        else:
            return False
