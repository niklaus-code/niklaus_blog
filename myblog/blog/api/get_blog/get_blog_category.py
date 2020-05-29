# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import com_model, token_model


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument('category', type=int, required=True, default = "python")
        self.get_args.add_argument('page_num', type=int, required=False, default = 0)
        self.args = self.get_args.parse_args()

    def get(self):
        token = token_model.Token()
        category = self.args['category']
        page_num = self.args['page_num'] - 1

        istance = com_model.Blog()
        blog_obj = istance.get_blog_category(category)

        res = []
        for blog in blog_obj:
            blog_dict = {}
            blog_dict["id"] = blog[0]
            blog_dict["title"] = blog[1]
            blog_dict["content"] = blog[2]
            blog_dict["author"] = blog[3]
            blog_dict["create_time"] = str(blog[4])
            blog_dict["like_number"] = blog[5]
            #blog_dict["signature"] = token.md5_method(token.b64(blog[0]))
            res.append(blog_dict)

        # 对读书首页blog分页
        group_num = 5 # 每页的数量
        len_blog = len(res)
        total_num = len_blog/5+1 if len_blog%5 > 0 else len_blog/5
        if category == 6:
            chil_list = []
            chil_list.append(group_num*page_num)
            chil_list.append(group_num*(page_num+1))
            blog_list = res[chil_list[0]: chil_list[1]]
            res = {}
            res["total_num"] = total_num
            res["data"] = blog_list
        return res
