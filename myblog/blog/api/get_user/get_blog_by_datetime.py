# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import get_blog_by_date
from flask import make_response, jsonify
import json



class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument('date', type=str)
        self.args = self.get_args.parse_args()

    def post(self):
        date = self.args["date"]

        istance = get_blog_by_date.Blog()
        blog = istance.count_date()

        if date:
            blog = istance.get_blog(date)


        return {"data": blog}




