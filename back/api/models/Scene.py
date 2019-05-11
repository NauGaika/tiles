# -*- coding: utf-8 -*-
"""все классы связанные со сценами."""

import json
import os
import cv2 as cv
import random
from .Material import Material
from datetime import datetime
from .. import app, db
from ..common_scripts import create_file
from sqlalchemy import func
from ..magic import make_img


class Scene_category(db.Model):
    """класс с категориями сцен."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), nullable=False)
    scenes = db.relationship('Scene', backref="category", lazy=True)

    @classmethod
    def get_all_category_names(cls):
        """Получаем все имена категорий сцен."""
        to_post = []
        for cat in Scene_category.query.all():
            to_post.append({
                'id': cat.id,
                'name': cat.name
            })
        return to_post

    @classmethod
    def get_category_by_name(cls, name):
        """Получаем категорию по ее имени."""
        return cls.query.filter_by(name=name).first()


class Scene(db.Model):
    """класс со сценами."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('scene_category.id'))
    planes = db.relationship('Plane', backref="scene", lazy=True)
    date = db.Column(db.DateTime)

    @classmethod
    def get_default_material(cls):
        return Material.query.first()

    @classmethod
    def next_id(cls):
        """следующий id."""
        max_id = db.session.query(func.max(cls.id)).first()[0]
        if not max_id:
            return 1
        return max_id+1

    @classmethod
    def create(cls, request):
        """Создание новой сцены."""
        shadow = request.files['shadow']
        light = request.files['light']
        img = request.files['img']
        category = str(request.form['category'])
        name = str(request.form['name'])
        point_count = len(request.files) - 3
        points = []
        category = Scene_category.get_category_by_name(category)
        new_scene_obj = cls(name=name, date=datetime.now(), category=category)
        db.session.add(new_scene_obj)
        db.session.commit()

        for i in range(0, point_count):
            points.append({
                'points': request.form['points_'+str(i)],
                'width': request.form['realWidth_'+str(i)],
                'height': request.form['realHeight_'+str(i)],
                'mask': request.files['mask_'+str(i)]
            })

        for point in points:
            plane_obj = Plane.create(
                                    point['points'],
                                    point['width'],
                                    point['height'])

            new_scene_obj.planes.append(plane_obj)
            create_file(point['mask'],
                        app.config['FOLDER_SCENE'],
                        prefix="plane_" + str(plane_obj.id),
                        number=new_scene_obj.id,
                        subfolder=True,
                        subfolder_name="scene")

        db.session.commit()
        create_file(img,
                    app.config['FOLDER_SCENE'],
                    preview=True,
                    prefix="scene",
                    number=new_scene_obj.id,
                    subfolder=True,
                    preview_width=500,
                    subfolder_name="scene")
        create_file(shadow,
                    app.config['FOLDER_SCENE'],
                    prefix="shadow",
                    number=new_scene_obj.id,
                    subfolder=True,
                    subfolder_name="scene")
        create_file(light,
                    app.config['FOLDER_SCENE'],
                    prefix="light",
                    number=new_scene_obj.id,
                    subfolder=True,
                    subfolder_name="scene")

        return json.dumps({
            'id': new_scene_obj.id
        })

    @classmethod
    def get_all_scene_by_category(cls, category):
        """получаем все сцены по имени категории."""
        category = str(category)
        all_scene = Scene_category.query.filter_by(name=category).first()
        all_scene = all_scene.scenes
        ret_obj = []
        for scene in all_scene:
            ret_obj.append({
                'id': scene.id,
                'name': scene.name
            })
        return json.dumps(ret_obj)

    @classmethod
    def get_all_points_from_scene(cls, elem_id):
        elem_id = int(elem_id)
        scene = cls.query.get(elem_id)
        data_to_send = []
        if scene:
            for plane in scene.planes:
                data_to_send.append([json.loads(plane.points)] + [plane.id])
            return json.dumps(data_to_send)
        return ''

    @classmethod
    def session_create(cls):
        return str(int(float(datetime.timestamp(datetime.now())) * 1000000))

    @classmethod
    def get_scene_img_by_id(cls, sceneId, filename="scene"):
        imgPath = os.path.join(app.config['FOLDER_SCENE'],
                               'scene_' + str(sceneId) + '/' + filename + '.png')
        img = cv.imread(imgPath)
        return img

    @classmethod
    def session_save_img(cls, img, session):
        imgPath = os.path.join(app.config['FOLDER_SESSION'], session + '.png')
        cv.imwrite(imgPath, img)
        return imgPath

    @classmethod
    def session_get_img(cls, session):
        imgPath = os.path.join(app.config['FOLDER_SESSION'], session + '.png')
        img = cv.imread(imgPath)
        return img

    @classmethod
    def get_material_image(cls, matId):
        imgPath = os.path.join(app.config['FOLDER_MATERIAL'],
                               'material_' + str(matId) + '.png')
        img = cv.imread(imgPath)
        return img

    @classmethod
    def get_mask_by_id(cls, sceneId, poligonId):
        imgPath = os.path.join(app.config['FOLDER_SCENE'],
                               'scene_' + str(sceneId) + \
                               '/plane_' + str(poligonId) + '.png')
        # print(imgPath)
        img = cv.imread(imgPath)
        return img

    @classmethod
    def design(cls, request):
        sceneId = int(request.form['sceneId'])
        poligonId = request.form['poligonId']
        materialId = request.form['materialId']
        session = request.form['session']
        if session == 'false':
            session = cls.session_create()
            bg = cls.get_scene_img_by_id(sceneId)
        else:
            session = str(session)
            bg = cls.session_get_img(session)

        points = Plane.get_points_by_id(poligonId)
        material_img = cls.get_material_image(materialId)
        mask = cls.get_mask_by_id(sceneId, poligonId)
        real_dimension = Plane.get_real_dimensions(poligonId)
        light = cls.get_scene_img_by_id(sceneId, filename="light")
        shadow = cls.get_scene_img_by_id(sceneId, filename="shadow")
        tile = Material.query.get(materialId)
        tile_dimensions = (tile.width, tile.height)
        # print(mask)
        img = make_img(bg, material_img, tile_dimensions, real_dimension[0],
                       real_dimension[1], points,
                       mask, shadow, light, tile.reflect / 100)
        cls.session_save_img(img, session)
        return session

    @classmethod
    def check(cls, request):
        """Проверяем создаваемую сцену"""
        shadow = request.files['shadow']
        light = request.files['light']
        img = request.files['img']
        point_count = len(request.files) - 3
        points = []
        for i in range(0, point_count):
            points.append({
                'points': request.form['points_'+str(i)],
                'width': request.form['realWidth_'+str(i)],
                'height': request.form['realHeight_'+str(i)],
                'mask': request.files['mask_'+str(i)]
            })
        temp_file_count = len([name for name in os.listdir(app.config['FOLDER_TEMP_SCENE']) if
                               os.path.isfile(os.path.join(app.config['FOLDER_TEMP_SCENE'], name))]) + 1
        scene = create_file(img,
                            app.config['FOLDER_TEMP_SCENE'],
                            prefix="scene",
                            number=temp_file_count)
        shadow = create_file(shadow,
                             app.config['FOLDER_TEMP_SCENE'],
                             prefix="shadow",
                             number=temp_file_count)
        light = create_file(light,
                            app.config['FOLDER_TEMP_SCENE'],
                            prefix="light",
                            number=temp_file_count)
        scene_img = cv.imread(scene)
        shadow_img = cv.imread(shadow)
        light_img = cv.imread(light)
        material = cls.get_default_material()
        material_img = cls.get_material_image(material.id)
        img = scene_img
        for point in points:
            temp_mask = create_file(point['mask'],
                                    app.config['FOLDER_TEMP_SCENE'],
                                    prefix="plane_" + str(temp_file_count),
                                    number=temp_file_count)
            mask_img = cv.imread(temp_mask)
            img = make_img(img, material_img, (material.width, material.height),
                           int(point['width']),
                           int(point['height']), json.loads(point['points']),
                           mask_img, shadow_img, light_img,
                           material.reflect / 100)
            os.remove(temp_mask)
        os.remove(shadow)
        os.remove(light)

        cv.imwrite(scene, img)

        return str('/img/temp/scene/scene_'+str(temp_file_count)+'.png?' + str(random.randint(0,1000)))

    @classmethod
    def checkMaterial(cls, request):
        """Создаем тестовую сцену для проверки материала"""

        sceneId = int(request.form['sceneId'])
        widht = int(request.form['width'])
        height = int(request.form['height'])
        reflect = float(request.form['reflect'])
        material_img = request.files['file']

        points = json.loads(cls.get_all_points_from_scene(sceneId))
        scene = cls.get_scene_img_by_id(sceneId)
        DIR = app.config['FOLDER_TEMP_MATERIAL']
        temp_file_count = len([name for name in os.listdir(DIR) if
                               os.path.isfile(os.path.join(DIR, name))]) + 1
        res = create_file(material_img,
                          DIR,
                          prefix="material",
                          number=temp_file_count)

        light = cls.get_scene_img_by_id(sceneId, filename="light")
        shadow = cls.get_scene_img_by_id(sceneId, filename="shadow")
        material_img = cv.imread(res)
        os.remove(res)

        for point in points:
            mask = cls.get_mask_by_id(sceneId, point[1])
            real_dimension = Plane.get_real_dimensions(point[1])
            img = make_img(scene, material_img, (widht, height), real_dimension[0],
                           real_dimension[1], Plane.get_points_by_id(point[1]),
                           mask, shadow, light, reflect / 100)
        cv.imwrite(res, img)

        return str('/img/temp/material/material_'+str(temp_file_count)+'.png')

    @classmethod
    def del_by_id(cls, elId):
        el = cls.query.get(elId)
        if el:
            db.session.delete(el)
            db.session.commit()
        return 'сцена удалена'
class Plane(db.Model):
    """Класс с плоскостями."""

    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Text)
    scene_id = db.Column(db.Integer, db.ForeignKey('scene.id'))
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)

    @classmethod
    def create(cls, points, width, height):
        """создаем новую плоскость."""
        points = points
        width = int(width)
        height = int(height)
        plane = cls(points=points, width=width, height=height)
        db.session.add(plane)
        db.session.commit()
        return plane

    @classmethod
    def get_points_by_id(cls, id):
        id = int(id)
        return json.loads(cls.query.get(id).points)

    @classmethod
    def get_real_dimensions(cls, id):
        id = int(id)
        plane = cls.query.get(id)
        return (plane.width, plane.height)
