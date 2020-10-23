# -*- coding: utf-8 -*-
import os
from application import create_app
from application import db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

# 设置默认模式
app = create_app(os.getenv('TYPE', 'default'))
host = app.config.get('HOST')
port = app.config.get('POST')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('runserver', Server(host=host, port=port))
manager.add_command('database', MigrateCommand)

if __name__ == '__main__':
    manager.run()
