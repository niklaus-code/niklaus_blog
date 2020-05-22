# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from datetime import datetime, timedelta
from flask import make_response
from flask import redirect
from ...commons import login_model, token_model


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument('email', type=str, required=False)
        self.get_args.add_argument('passwd', type=int, default=0, required=False)
        self.get_args.add_argument('token', type=str, required=False, default='', location=['cookies'])
        self.args = self.get_args.parse_args()

    def post(self):
        now = datetime.now()
        expire = now + timedelta(days=30)
        email = self.args['email']
        passwd = self.args['passwd']
        token = self.args['token']

        is_token = token_model.Token()
        auth_token = is_token.auth_token(token)
        if auth_token:
            return make_response("1")

        inst = token_model.Token()
        token_str = inst.generate_token(email)

        istance = login_model.Login()
        res = istance.user_login(email, passwd, now)

        if res:
            response = make_response("1")
            response.set_cookie('token', token_str, expires=expire)
            return response
        else:
            response = make_response("0")
            return response
