# -*- coding: utf-8 -*-
"""все что относится к работе с материалами."""

# import sys
# import json
from .. import db, app
from ..common_scripts import create_file
from sqlalchemy import func
# from .Word_associate import Word_associate
# from sqlalchemy import and_


class Material_category(db.Model):
    """Категории материалов."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), nullable=False)
    materials = db.relationship('Material', backref="category", lazy=True)

    @classmethod
    def create(cls, name):
        """Создание новой категории материалов."""
        name = str.strip(str(name))
        mat_obj = cls(name=name)
        db.session.add(mat_obj)
        return mat_obj

    @classmethod
    def get_category_by_name(cls, name):
        """Получаем категорию по имени."""
        return cls.query.filter_by(name=name).first()

    @classmethod
    def get_all_category_names(cls):
        """получаем имена всех доступных категорий."""
        to_post = []
        for cat in cls.query.all():
            to_post.append({
                'id': cat.id,
                'name': cat.name
            })
        return to_post


class Material(db.Model):
    """Класс материалов."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(240), nullable=False, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('material_category.id'))
    article = db.Column(db.String(30), nullable=False, unique=True)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    reflect = db.Column(db.Integer, nullable=False)

    @classmethod
    def max_id(cls):
        max_id = db.session.query(func.max(cls.id)).first()[0]
        if not max_id:
            return 1
        return max_id

    @classmethod
    def generate_article(cls):
        return 'МАТ' + str(cls.max_id())

    @classmethod
    def create(cls, name, category, article, width, height, reflect, file):
        """Создание нового материала."""
        if not cls.query.filter_by(name=name).first():
            category = str.strip(str(category))
            category_obj = Material_category.get_category_by_name(category)

            name = str.strip(str(name))
            article = str.strip(str(article).lower())
            width = abs(int(width))
            height = abs(int(height))
            reflect = abs(int(float(reflect.replace(',', '.'))))

            if not category_obj:
                category_obj = Material_category.create(category)
            if not article:
                article = cls.generate_article()
            if (name and category_obj and article and width and height):
                material_obj = cls(name=name,
                                   category=category_obj,
                                   article=article,
                                   width=width,
                                   height=height,
                                   reflect=reflect,
                                   )
                db.session.add(material_obj)
                db.session.commit()

                create_file(file,
                            app.config['FOLDER_MATERIAL'],
                            preview=True,
                            prefix="material",
                            number=material_obj.id)
                return 'Материал добавлен'
        return 'материал не добавлен'

    @classmethod
    def get_all_material_by_category(cls, cat_name):
        arr_to_send = []
        cat_name = str(cat_name)
        category = Material_category.get_category_by_name(cat_name)
        if category:
            res = category.materials
            for mat in res:
                arr_to_send.append({
                    'id': mat.id,
                    'article': mat.article,
                    'category': mat.category.name,
                    'name': mat.name,
                    'dimensions': (mat.width, mat.height),
                })
        return arr_to_send

    @classmethod
    def delete_by_id(cls, elem_id):
        el = cls.query.get(elem_id)
        if el:
            db.session.delete(el)
            db.session.commit()
        return 'Материал удален'
