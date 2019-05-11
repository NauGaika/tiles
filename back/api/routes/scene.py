# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import request
from ..models import Scene_category, Scene
import json

Scene_api = Blueprint('Scene_api', __name__)


@Scene_api.route('/scene/category/get_all_names', methods=['GET', 'POST'])
def new_dict():
    """create new dict for user """
    if request.method == "GET":
        return json.dumps(Scene_category.get_all_category_names())

@Scene_api.route('/scene/create', methods=['GET', 'POST'])
def new_scene():
    """Create new scene"""
    if request.method == "POST":
        return Scene.create(request)

@Scene_api.route('/scene/getByCategory', methods=['GET', 'POST'])
def get_scene_by_category():
    """Get all scene by category name"""
    if request.method == "GET":
        category = request.args['category']
        return Scene.get_all_scene_by_category(category)

@Scene_api.route('/scene/getAllPlanePoints', methods=['GET', 'POST'])
def get_all_points_from_scene():
    """Get all scene planes"""
    if request.method == "GET":
        elem_id = request.args['id']
        return Scene.get_all_points_from_scene(elem_id)

@Scene_api.route('/scene/design', methods=['GET', 'POST'])
def design_scene():
    """Get all scene planes"""
    if request.method == "POST":
        return Scene.design(request)

@Scene_api.route('/scene/check', methods=['GET', 'POST'])
def check_scene():
    """Check scene before create"""
    if request.method == "POST":
        return Scene.check(request)

@Scene_api.route('/scene/deleteById', methods=['GET', 'POST'])
def del_scene_by_id():
    """удаляем сцену по id"""
    if request.method == "GET":
        return Scene.del_by_id(int(request.args['sceneId']))
