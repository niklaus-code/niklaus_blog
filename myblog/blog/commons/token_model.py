# coding=utf-8
import base64
import hashlib
from datetime import datetime, timedelta


class Token(object):

    def __init__(self):
        self.secret = "passwd"

    def generate_token(self, username):
        if not username:
            return False
        md5_pw = self.md5_method(self.secret)

        now = datetime.now()
        now_5 = datetime.now()+timedelta(minutes=5)
        token_dict = {
            "iat": now,
            "exp": now_5,
            "user": username,
            }
        encode_str = base64.b64encode(str(token_dict))+"()"+md5_pw
        return encode_str

    def md5_method(self, str):
        md5 = hashlib.md5()
        md5_str = ""
        if str:
            md5.update(str)
            md5_str = md5.hexdigest()
        return md5_str

    def auth_token(self, token):
        if not token:
            return False
        str_token = token.split("()")
        if str_token[1] != self.md5_method(self.secret):
            return False
        str_token_json = base64.b64decode(str_token[0])
        return True

    def b64(self, item):
        b64_str = ''
        if item:
            b64_str = base64.b64encode(str(item))
            b64_str = base64.b64encode(str(item))
        return b64_str
