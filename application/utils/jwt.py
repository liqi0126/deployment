# -*- coding: utf-8 -*-
import jwt
from flask import current_app
import datetime
import hashlib
import scrypt
import base64

def generate_jwt(payload, expiry=None):
    """
    
    :param payload: dict 载荷
    :param expiry: datetime 有效期
    :return: 生成jwt
    """
    if expiry == None:
        now = datetime.datetime.now()
        expire_hours = int(current_app.config.get('JWT_EXPIRE_HOURS'))
        expiry = now + datetime.timedelta(hours=expire_hours)

    _payload = {'exp': expiry}
    _payload.update(payload)

    secret = current_app.config.get('JWT_SECRET', '')

    token = jwt.encode(_payload, secret, algorithm='HS256')
    return token.decode()

def verify_jwt(token):
    """
    校验jwt
    :param token: jwt
    :return: dict: payload
    """
    secret = current_app.config.get('JWT_SECRET', '')

    try:
        payload = jwt.decode(token, secret, algorithm=['HS256'])
    except jwt.PyJWTError:
        payload = None

    return payload

def encrypt_password(password):
    salt = current_app.config.get('SALT', '')
    key = scrypt.hash(password, salt, 32768, 8, 1, 32)
    return base64.b64encode(key).decode("ascii")
