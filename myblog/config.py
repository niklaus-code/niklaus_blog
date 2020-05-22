# coding=utf-8
import os


class Config(object):
    secret_key = "123456"
    DATABASE_URI = ""
    REDIS_URI = "flask:3306"

class ProductionConfig(Config):
    secret_key = "123456"
    REDIS_URI = "mysql:3306"
    db_conn = {
        "DATABASE_NAME": "myblog",
        "DATABASE_URI": "127.0.0.1",
        "DATABASE_PORT": "3306",
        "DATABASE_USER": "ysman",
        "DATABASE_passwd": "123456"
        }

class TestConfig(Config):
    secret_key = "123456"
    REDIS_URI = "127.0.0.1:3306"
    db_conn = {
        "DATABASE_NAME": "myblog",
        "DATABASE_URI": "127.0.0.1",
        "DATABASE_PORT": "3306",
        "DATABASE_USER": "ysman",
        "DATABASE_passwd": "123456",
        }

config_dict = {
    "pro": ProductionConfig,
    "test": TestConfig
    }

config = config_dict.get(os.getenv("env"), "pro")
