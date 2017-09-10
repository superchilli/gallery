# -*- coding: utf-8 -*-

import os
import time
import bleach
import PIL
import hashlib

from PIL import Image
from flask import render_template, redirect, url_for, flash, abort, request, current_app, \
    send_from_directory
from flask_login import login_required, current_user

from . import main
from .forms import EditProfileAdminForm, CommentForm,\
    AddPhotoForm, SettingForm
from .. import db, photos
from ..models import User, Role, Photo, Permission, LikeAlbum, LikePhoto,\
    Comment, Follow
from ..decorators import admin_required, permission_required

@main.route('/', methods=['GET','POST'])
def index():
    if current_user.is_authenticated:
        photos=current_user.followed_photos
    else:
        photos=""
    return render_template('index.html', photos=photos)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/return-files', methods=['GET'])
def return_file():
    return send_from_directory(directory='static', filename='styles.css', as_attachment=True)

@main.route('/explore', methods=['GET', 'POST'])
def explore():
    photos=Photo.query.order_by(Photo.timestamp.desc()).all()
    photos=[photo for photo in photos if photo.author != current_user]
    photo_type="new"
    return render_template('explore.html', photos=photos, type=photo_type)

@main.route('/explore/hot', methods=['GET', 'POST'])
def explore_hot():
    photos=Photo.query.all()
    result={}
    for photo in photos:
        result[photo]=len(list(photo.photo_liked)) # result={"photo1": 10,}
    # sorted dict with the photo likeed numbers, reverse the result
    # [('photo9', 100), ('photo3': 70),... ]
    sorted_photo=sorted(result.items(), key=lambda x:x[1], reverse=True)
    temp=[]
    for photo in sorted_photo: # ('photo9': 100)
        temp.append(photo[0]) # 'photo9'
    photo.type="hot"
    return render_template('explore.html', photos=temp, type=photo.type)








