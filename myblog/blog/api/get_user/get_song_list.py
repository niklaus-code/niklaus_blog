# coding=utf-8
from flask_restful import Resource
from flask_restful import reqparse
from ...commons import music_model


class Api(Resource):
    def __init__(self):
        self.get_args = reqparse.RequestParser()
        self.args = self.get_args.parse_args()

    def post(self):
        music_obj = music_model.Music()
        song_list = music_obj.get_song_list()
        music_list = []
        for music in song_list:
            music_dict = {}
            music_dict["name"] = music[0]
            music_dict["url"] = music[1]
            music_list.append(music_dict)
        return music_list
