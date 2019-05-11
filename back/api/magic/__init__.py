# -*- coding: utf-8 -*-
"""Класс создающий картинки."""

import json
import cv2
import math
import time
import numpy as np
import itertools as IT
import os
import random


def make_img(bg, tile, tile_dimensions, width, height, pts,
             mask, shadow, light, intens):
    """функция создающая изображение."""
    # print(intens)
    pts2 = np.float32(pts)
    img = create_img_by_length(width, height, tile, tile_dimensions, pts)
    img = deform_img_to_point(img, pts2, bg.shape)
    img = add_shadow(img, shadow)
    img = add_mask(img, mask)
    img = add_light(img, light, intens=intens)
    img = overlay_transparent(bg, img, 0, 0)
    return img


def overlay_transparent(background, overlay, x, y):
    """функция создающая изображение."""
    background_width = background.shape[1]
    background_height = background.shape[0]

    if x >= background_width or y >= background_height:
        return background

    h, w = overlay.shape[0], overlay.shape[1]

    if x + w > background_width:
        w = background_width - x
        overlay = overlay[:, :w]

    if y + h > background_height:
        h = background_height - y
        overlay = overlay[:h]

    if overlay.shape[2] < 4:
        overlay = np.concatenate(
            [
                overlay,
                np.ones((overlay.shape[0], overlay.shape[1], 1),
                        dtype=overlay.dtype) * 255
            ],
            axis=2,
        )

    overlay_image = overlay[..., :3]
    mask = overlay[..., 3:] / 255.0

    background[y:y+h, x:x+w] = (1.0 - mask) * background[y:y+h, x:x+w] \
        + mask * overlay_image

    return background


def to_rgba(img):
    """добавляем альфа канал."""
    b_channel, g_channel, r_channel = cv2.split(img)
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255
    img = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    return img


def get_max_el(pts):
    max_p = np.max(pts, 0)
    min_p = np.min(pts, 0)

    leng = max_p - min_p

    return leng.astype(np.int)


def deform_img_to_point(img, pts2, bg):
    """Преобразует данное изображение к точкам."""
    max_width = max(img.shape[0], bg[0])
    max_height = max(img.shape[1], bg[1])

    pts1 = np.float32([
        [0, 0],
        [img.shape[1], 0],
        [img.shape[1], img.shape[0]],
        [0, img.shape[0]]
    ])
    # print(pts1)
    # print(pts2)
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    res = cv2.warpPerspective(img, matrix, (max_height, max_width))
    return res


def add_mask(img, mask):
    """Добавляет маску. Нужно переработать."""
    img = img[0:mask.shape[0], 0:mask.shape[1]]
    img = img.astype(np.float) / 255
    mask = mask.astype(np.float) / 255
    img_r, img_g, img_b, img_a = cv2.split(img)
    mask_r, mask_g, mask_b = cv2.split(mask)
    new_img_a = (mask_r + mask_g + mask_b) / 3
    new_img_a = np.minimum(img_a, new_img_a)
    img = cv2.merge((img_r * 255, img_g * 255, img_b * 255, new_img_a * 255))
    return img


def add_light(img, light, intens=1):
    """добавляет свет."""
    n_s = light.astype(np.float32) / 255
    n_i = img.astype(np.float32) / 255
    n_i = n_i[0:n_s.shape[0], 0:n_s.shape[1]]
    r_s, g_s, b_s = cv2.split(n_s)
    r_i, g_i, b_i, b_a = cv2.split(n_i)
    n_b_i = 1 - (1 - b_s * intens) * (1 - b_i)
    n_g_i = 1 - (1 - g_s * intens) * (1 - g_i)
    n_r_i = 1 - (1 - r_s * intens) * (1 - r_i)
    n_a_i = b_a
    img = cv2.merge((n_r_i * 255, n_g_i * 255, n_b_i * 255, n_a_i * 255))
    return img


def add_shadow(img, shadow):
    """добавляет тень."""
    n_s = shadow.astype(np.float32) / 255
    n_i = img.astype(np.float32) / 255
    n_i = n_i[0:n_s.shape[0], 0:n_s.shape[1]]
    r_s, g_s, b_s = cv2.split(n_s)
    r_i, g_i, b_i, b_a = cv2.split(n_i)
    n_b_i = b_s * b_i
    n_g_i = g_s * g_i
    n_r_i = r_s * r_i
    n_a_i = b_a
    img = cv2.merge((n_r_i * 255, n_g_i * 255, n_b_i * 255, n_a_i * 255))
    return img


def create_img_by_length(width, height, tile, tile_dimensions, pts):
    """Создает сразу набор плиток на стену."""
    dim_elem = get_max_el(pts)
    count_of_width = width / tile_dimensions[0]
    count_of_height = height / tile_dimensions[1]
    koef_width = dim_elem[0] / count_of_width / tile_dimensions[0]
    koef_height = dim_elem[1] / count_of_height / tile_dimensions[1]
    if koef_width > koef_height:
        tile_width = tile_dimensions[0] * koef_width
        tile_height = tile_dimensions[1] * koef_width
    else:
        tile_width = tile_dimensions[0] * koef_height
        tile_height = tile_dimensions[1] * koef_height
    tile_width = int(tile_width)
    tile_height = int(tile_height)
    tile = cv2.resize(
        tile,
        (tile_width, tile_height),
        interpolation=cv2.INTER_NEAREST)
    img_width = int(count_of_width * tile_width)
    img_height = int(count_of_height * tile_height)
    canvas = np.zeros((img_height, img_width, 3), np.uint8)
    for numer_column in range(math.ceil(count_of_height)):
        for number_line in range(math.ceil(count_of_width)):
            input_height_start = tile_height * numer_column
            input_width_start = tile_width * number_line
            input_height_finish = input_height_start + tile_height
            input_width_finish = input_width_start + tile_width
            _tile_height = tile_height
            _tile_width = tile_width
            if input_width_finish > img_width:
                _tile_width = tile_width - (input_width_finish - img_width)
                input_width_finish = img_width
            if input_height_finish > img_height:
                _tile_height = _tile_height - input_height_finish + img_height
                input_height_finish = input_height_start + _tile_height
            # canvas_region = canvas[input_height_start: input_height_finish,
            #                        input_width_start: input_width_finish]
            # tile_region = tile[0: _tile_height, 0: _tile_width]
            canvas[input_height_start: input_height_finish,
                   input_width_start: input_width_finish] = tile[
                0: _tile_height, 0: _tile_width]
    canvas = to_rgba(canvas)
    return canvas
