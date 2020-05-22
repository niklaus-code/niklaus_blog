# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import com_model
from flask import make_response, jsonify
import json



class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument('title', type=str)
        self.get_args.add_argument('content', type=str)
        self.args = self.get_args.parse_args()

    def post(self):

        istance = com_model.Blog()
        blog = istance.get_blog()

        init_list = []
        for i in blog:
            i = list(i)
            i[4] = str(i[4])
            init_list.append(i)

        if blog:
            return {"name": init_list}
        else:
            return False



