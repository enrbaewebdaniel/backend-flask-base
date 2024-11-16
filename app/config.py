import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", f"sqlite:///{os.path.join(BASE_DIR, '../data.sqlite')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
