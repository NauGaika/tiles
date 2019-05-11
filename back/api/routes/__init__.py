# -*- coding: utf-8 -*-
from flask import Flask, flash, request
from .. import app, db
from .material import Material_api
from .scene import Scene_api
from ..models import Material, Scene, Scene_category, Plane, Material_category


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Material': Material,
        'Material_category': Material_category,
        'Scene': Scene,
        'Scene_category': Scene_category,
        'Plane': Plane
    }


app.register_blueprint(Material_api)
app.register_blueprint(Scene_api)
