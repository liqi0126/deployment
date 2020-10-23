# -*- coding: utf-8 -*-

from application.extensions import db
from datetime import datetime


class User(db.Model):
    """
    论坛用户
    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, doc="用户id")

    username = db.Column(db.String(32), unique=True, doc="账号")
    password = db.Column(db.String(255), doc="密码")
    nickname = db.Column(db.String(255), doc="用户名称")

    document_number = db.Column(db.String(255), doc="身份证号")
    mobile = db.Column(db.String(255), doc="手机号")
    email = db.Column(db.String(255), doc="邮箱")

    created = db.Column(db.DateTime, doc="创建时间")
    updated = db.Column(db.DateTime, doc="更新时间")


class Post(db.Model):
    """
    帖子
    """
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, doc="帖子id")

    user_id = db.Column(db.Integer, doc="发帖用户id")

    title = db.Column(db.String(255), doc="帖子标题")
    content = db.Column(db.String(255), doc="帖子内容")

    last_replied_user_id = db.Column(db.Integer, doc="最新回复的用户id")
    last_replied_time = db.Column(db.DateTime, doc="最新回复时间")

    created = db.Column(db.DateTime, doc="创建时间")
    updated = db.Column(db.DateTime, doc="更新时间")


class Reply(db.Model):
    """
    回复
    """
    __tablename__ = 'reply'

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, doc="回复id")

    user_id = db.Column(db.Integer, doc="回复用户id")
    post_id = db.Column(db.Integer, doc="回复帖子id")
    reply_id = db.Column(db.Integer, doc="回复帖子id")

    content = db.Column(db.String(255), doc="帖子内容")

    created = db.Column(db.DateTime, doc="创建时间")
    updated = db.Column(db.DateTime, doc="更新时间")
