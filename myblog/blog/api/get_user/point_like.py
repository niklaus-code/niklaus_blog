# coding=utf-8
# 点赞API

from flask_restful import Resource
from flask_restful import reqparse
from ...commons import com_model


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument('id', type=int)
        self.args = self.get_args.parse_args()

    def post(self):
        istance = com_model.Blog()
        point = istance.point_like(self.args['id'])
        if point:
            return {"point_like": point}
        else:
            return False
