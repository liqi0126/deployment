# -*- coding: utf-8 -*-
import os
from flask import Flask
from application.controllers import blueprints
from application.configs import configs
from application.extensions import db
from application.utils import jwt_authentication, settings


def init_extensions(app):
    db.init_app(app)


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('TYPE', 'default')

    app = Flask(__name__)
    app.config.from_object(configs[config_name])
    app.before_request(jwt_authentication)

    init_extensions(app)

    # blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    db.init_app(app)
    db.create_all()

    return app
