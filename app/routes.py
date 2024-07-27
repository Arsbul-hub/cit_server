import os

from flask import render_template, send_from_directory, url_for, flash, redirect, request

from PIL import Image
from flask_login import current_user, login_user, logout_user, login_required

from app import application


def load_file(name):
    try:
        return Image.open("app/" + name)

    except FileNotFoundError:
        return None



@application.route('/files/<path:filename>')
def uploaded_files(filename):
    return send_from_directory("static/loaded_media", filename)


@application.route('/')
def index():

    return "hello"

@application.errorhandler(404)
def page_not_found(error):
    return "404", 404
