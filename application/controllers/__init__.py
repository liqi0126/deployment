# -*- coding: utf-8 -*-

from application.controllers import (
    user,
    hello,
    post
)

blueprints = [
    user.bp,
    hello.bp,
    post.bp
]
