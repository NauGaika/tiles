# -*- coding: utf-8 -*-
from flask import Flask
from .conf import Config
import os
import sys

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import models, routes
