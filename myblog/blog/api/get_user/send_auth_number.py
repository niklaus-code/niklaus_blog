# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import sendmail, login_model
import random


class Api(Resource):
    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument('email', type=str, required=True)
        self.args = self.get_args.parse_args()

    def post(self):
        email = self.args['email']
        if not email:
            return {"code": 9001}

        number = random.randint(99999, 1000000)
        instance_record = login_model.Login()
        record_mail = instance_record.login_record(email, number)

        instance = sendmail.Mail()
        res = instance.send_mail(email, number)

        if res and record_mail:
            return {'code': 200}
        return {"code": 9001}
