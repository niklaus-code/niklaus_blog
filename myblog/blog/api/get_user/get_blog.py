# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import com_model
from ...commons import token_model
from flask import jsonify


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument('offset', type=int, default=10)
        self.get_args.add_argument('start', type=int, default=1)
        self.args = self.get_args.parse_args()

    def get(self):
        offset = self.args["offset"]
        start = self.args["start"]
        startpage = (start-1)*offset

        is_token = token_model.Token()
        obj_blog = com_model.Blog()
        allblog = obj_blog.get_blog(startpage, offset)
        totalnumber = obj_blog.get_total_number(offset)

        bloglist = []
        for blog in allblog:
                blog_dict = {}
                blog_dict["id"] = blog[0]
                blog_dict["title"] = blog[1]
                blog_dict["content"] = blog[2]
                blog_dict["img"] = blog[3]
                blog_dict["category"] = blog[4]
                #blog_dict["signature"] = is_token.md5_method(is_token.b64(blog[0]))
                bloglist.append(blog_dict)
        res = {}
        res["totalnumber"] = totalnumber
        res["bloglist"] = bloglist
        return res
