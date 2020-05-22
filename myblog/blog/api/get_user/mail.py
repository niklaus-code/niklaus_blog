# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import login_model
from flask import make_response
import random


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument('email', type=str)
        self.args = self.get_args.parse_args()

    def post(self):
        email = self.args['email']
        number = random.randint(99999, 1000000)

        instance = login_model.Login()
        res = instance.login_record(email, number)

        if res:
            return {'number': number}
        else:
            return []
