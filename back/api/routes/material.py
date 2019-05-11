# -*- coding: utf-8 -*-
import json
from flask import Blueprint, request, render_template
from ..models import Material, Material_category, Scene

Material_api = Blueprint('Material_api', __name__)


@Material_api.route('/material/create', methods=['GET', 'POST'])
def new_material():
    """Create new material."""
    if request.method == "POST":
        file = request.files['file']
        category = request.form['category']
        name = request.form['name']
        article = request.form['article']
        width = request.form['width']
        height = request.form['height']
        reflect = request.form['reflect']
        create_result = Material.create(name, category, article, width, height, reflect, file)
        return create_result
    return ""

@Material_api.route('/material/category/get_all_names', methods=['GET', 'POST'])
def get_material_categorys():
    """Get all material category names."""
    return json.dumps(Material_category.get_all_category_names())

@Material_api.route('/material/getByCategory', methods=['GET', 'POST'])
def get_material_by_category():
    """Get all material category names."""
    category = request.args['category']
    return json.dumps(Material.get_all_material_by_category(category))

@Material_api.route('/material/deleteById', methods=['GET', 'POST'])
def deleteMaterialById():
    """DeleteMaterialById."""
    materialId = int(request.args['materialId'])
    if materialId:
        return Material.delete_by_id(materialId)

@Material_api.route('/material/check', methods=['GET', 'POST'])
def check_material():
    """Create file by user file temporary"""
    sceneId = int(request.form['sceneId'])
    widht = int(request.form['width'])
    height = int(request.form['height'])
    reflect = float(request.form['reflect'])
    file = request.files['file']
    if file:
        return Scene.checkMaterial(request)
    return ""
    # return json.dumps(Material.get_all_material_by_category(category))
