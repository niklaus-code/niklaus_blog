# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import us_prama


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.args = self.get_args.parse_args()

    def get(self):
        obj_prama = us_prama.UsPrama()
        prama= obj_prama.prama()

        return prama
