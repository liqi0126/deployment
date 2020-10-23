# -*- coding: utf-8 -*-
from flask import g

def login_required(func):
    """
    用户必须登录装饰器
    使用方法：放在method_decorators中
    """
    # @wraps(func)
    def wrapper(*args, **kwargs):
        if not g.user_id:
            return {'message': 'User must be authorized.'}, 401
        else:
            return func(*args, **kwargs)
    wrapper.__name__ = "warper" + func.__name__
    return wrapper
