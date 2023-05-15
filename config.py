import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "wikibooks.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER")
    POSTMARK_SERVER_TOKEN = os.environ.get("POSTMARK_SERVER_TOKEN")
    ELASTICSEARCH_URL = os.environ.get("ELASTICSEARCH_URL")
    ADMINS = ["amuriuki@olam-erp.com"]
    ELASTIC_USER = os.environ.get("ELASTIC_USER")
    ELASTIC_TOKEN = os.environ.get("ELASTIC_TOKEN")
    DOCUMENTS_PER_PAGE = 10
