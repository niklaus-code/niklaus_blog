from flask_restful import Resource, reqparse
from ...commons import com_model
from ...commons import token_model


class Api(Resource):

    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.get_args.add_argument('article_id', type=int, required=False)
        self.get_args.add_argument('action', type=str, required=True)
        self.get_args.add_argument('signature', type=str, required=False)
        self.args = self.get_args.parse_args()

    def post(self):
        top_article = com_model.Blog()
        is_token = token_model.Token()

        article_id = self.args["article_id"]
        action = self.args["action"]

        if action == "insert":
            res = top_article.top_list(article_id)

        allblog = top_article.get_blog()
        top_blogid = top_article.get_top_article_id()
        top_blog = top_article.get_top_blog_by_id(top_blogid)

        blog_list = []
        if top_blog:
            for blog in top_blog:
                blog_dict = {}
                blog_dict["id"] = blog[0]
                blog_dict["title"] = blog[1]
                blog_dict["content"] = blog[2]
                blog_dict["author"] = blog[3]
                blog_dict["time"] = str(blog[4])
                blog_dict["signature"] = is_token.md5_method(is_token.b64(blog[0]))
                blog_dict["top"] = True
                blog_dict["top_"] = False
                blog_list.append(blog_dict)

        for blog in allblog:
            blog_dict = {}
            blog_dict["id"] = blog[0]
            blog_dict["title"] = blog[1]
            blog_dict["content"] = blog[2]
            blog_dict["author"] = blog[3]
            blog_dict["time"] = str(blog[4])
            blog_dict["signature"] = is_token.md5_method(is_token.b64(blog[0]))
            blog_dict["top"] = False
            blog_dict["top_"] = True
            blog_list.append(blog_dict)

        return blog_list
