# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import com_model
from ...commons import token_model


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument("id", type=int, required=True)
        self.get_args.add_argument("signature", type=str, required=False)
        self.get_args.add_argument("category", type=str, required=False)
        self.args = self.get_args.parse_args()

    def post(self):
        id = self.args["id"]
        signature = self.args["signature"]
        category = self.args["category"]

        '''
        is_token = token_model.Token()
        if signature != is_token.md5_method(is_token.b64(id)):
            return {"res": 400}
        '''

        is_model = com_model.Blog()
        res = is_model.get_blog_info_by_id(id, category)
        return {"res": res}
