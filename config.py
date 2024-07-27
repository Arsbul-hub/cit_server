import json
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(
        os.path.abspath(os.path.dirname(__file__)), 'app.db')

    FLASKFILEMANAGER_FILE_PATH = "app/static/loaded_media"

    # FLASKFILEMANAGER_CUSTOM_CONFIG_JSON_PATH = "app/static/json/filemanager.config.json"
    JWS_SECRET_KEY = "sw.sef8-se8-e.3hb3-h318.wf-i3wfv_DRg11-3drgdr.gdrdr-drgdrg21211-drgdr3332drgsf.ef"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CKEDITOR_HEIGHT = 500
