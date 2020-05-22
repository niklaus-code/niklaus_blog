# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import comments_model, token_model
from flask import make_response, jsonify
import json


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument('comment', type=str)
        self.get_args.add_argument('article_id', type=int, default=1)
        self.get_args.add_argument('user_id', type=int, default=1)
        self.get_args.add_argument('parent_id', type=int, default=1)
        self.get_args.add_argument('token', type=str, default='', location=['cookies'])
        self.args = self.get_args.parse_args()

    def post(self):
        ist = comments_model.comments()
        ist_token = token_model.Token()

        token = self.args['token']
        auth_token = ist_token.auth_token(token)
        if auth_token:
            return auth_token

        insert = ist.insert_comments(self.args['comment'], self.args['article_id'], self.args['user_id'], self.args['parent_id'])

        if insert:
            # res = make_response(jsonify(dict))
            #rst.headers['Access-Control-Allow-Origin'] = '*'
            return {"res": "success"}
        else:
            return {"res": False}
