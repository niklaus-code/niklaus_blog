# coding=utf-8

from flask_restful import Resource
from flask_restful import reqparse
from ...commons import com_model
from flask import make_response, jsonify
import json


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument('id', type=int)
        self.args = self.get_args.parse_args()

    def post(self):
        istance = com_model.Blog()
        point = istance.commen_select_blog_info(self.args['id'])

        if point:
            return point[3]
        else:
            return 999
