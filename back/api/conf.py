# -*- coding: utf-8 -*-
"""Конфигурационный файл для фласк."""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Конфигурационный файл для фласк."""

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1111@localhost/tiles'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "../static/"
    FOLDER_MATERIAL = "../front/static/img/material"
    FOLDER_TEMP_MATERIAL = "../front/static/img/temp/material"
    FOLDER_TEMP_SCENE = "../front/static/img/temp/scene"
    FOLDER_SCENE = "../front/static/img/scene"
    FOLDER_SESSION = "../front/static/img/session"
