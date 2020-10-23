# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, current_app, jsonify, request, g
from application.utils import generate_jwt, login_required
from application.checkers import post_params_check, reply_post_params_check
from application.services import PostService

bp = Blueprint(
    'post',
    __name__,
    template_folder='../templates'
)

service = PostService()


@bp.route('/api/v1/post', methods=['GET'])
@login_required
def get_post_list():
    """
    获取帖子列表
    """
    page = 1 if request.args.get(
        'page') is None else int(request.args.get('page'))
    size = 10 if request.args.get(
        'size') is None else int(request.args.get('size'))
    user_id = 0 if request.args.get(
        'userId') is None else request.args.get('userId')
    order_by_reply = False if request.args.get(
        'orderByReply') is None else True
    post_list, count, result = service.get_post_list(
        user_id, page, size, order_by_reply)
    if result:
        return jsonify({
            'posts': post_list,
            'page': page,
            'size': size,
            'total': count
        }), 200
    else:
        return jsonify({'message': "error"}), 500


@bp.route('/api/v1/post', methods=['POST'])
@login_required
def add_post():
    """
    发帖
    """
    try:
        content = request.get_json()
        if content is None:
            return jsonify({'message': "bad arguments"}), 400
        key, passed = post_params_check(content)
        if not passed:
            return jsonify({'message': "invalid arguments: " + key}), 400

        id, result = service.create_post(content['title'],
                                         content['content'], g.user_id)

        if result:
            return jsonify({
                'postId': id,
                'message': "ok"
            }), 200
        else:
            return jsonify({'message': "error"}), 500
    except KeyError:
        return jsonify({'message': "bad arguments"}), 400
    else:
        return jsonify({'message': "error"}), 500


@bp.route('/api/v1/post/<int:postId>', methods=['GET'])
@login_required
def get_post_detail(postId):
    """
    获取帖子详情
    """
    detail, result = service.get_post_detail(postId)
    if result:
        return jsonify(detail), 200
    else:
        return jsonify({'message': "error"}), 500


@bp.route('/api/v1/post/<int:postId>', methods=['PUT'])
@login_required
def modify_post(postId):
    """
    修改帖子
    """
    try:
        content = request.get_json()
        if content is None:
            return jsonify({'message': "bad arguments"}), 400
        key, passed = post_params_check(content)
        if not passed:
            return jsonify({'message': "invalid arguments: " + key}), 400

        check = service.check_post(postId, g.user_id)
        if not check:
            return jsonify({'message': "not found"}), 404

        result = service.update_post(content['title'],
                                     content['content'], postId, g.user_id)

        if result:
            return jsonify({'message': "ok"}), 200
        else:
            return jsonify({'message': "error"}), 500
    except KeyError:
        return jsonify({'message': "bad arguments"}), 400
    else:
        return jsonify({'message': "error"}), 500


@bp.route('/api/v1/post/<int:postId>/reply', methods=['POST'])
@login_required
def reply_post(postId):
    """ 
    回复帖子
    """
    try:
        content = request.get_json()
        if content is None:
            return jsonify({'message': "bad arguments"}), 400

        key, passed = reply_post_params_check(content)
        if not passed:
            return jsonify({'message': "invalid arguments: " + key}), 400
        if "replyId" in content:
            reply_id = content['replyId']
        else:
            reply_id = 0

        check = service.check_reply(postId, reply_id)
        if not check:
            return jsonify({'message': "not found"}), 404

        result = service.create_reply(
            content['content'], g.user_id, postId, reply_id)

        if result:
            return jsonify({'message': "ok"}), 200
        else:
            return jsonify({'message': "error"}), 500
    except KeyError:
        return jsonify({'message': "bad arguments"}), 400
    else:
        return jsonify({'message': "error"}), 500


@bp.route('/api/v1/post/<int:postId>/reply/<int:replyId>', methods=['PUT'])
@login_required
def modify_reply(postId, replyId):
    """
    修改回复
    """
    try:
        content = request.get_json()
        if content is None:
            return jsonify({'message': "bad arguments"}), 400

        key, passed = reply_post_params_check(content)
        if not passed:
            return jsonify({'message': "invalid arguments: " + key}), 400

        check = service.check_self_reply(replyId, g.user_id)
        if not check:
            return jsonify({'message': "not found"}), 404

        result = service.update_reply(
            content['content'], g.user_id, postId, replyId)

        if result:
            return jsonify({'message': "ok"}), 200
        else:
            return jsonify({'message': "error"}), 500
    except KeyError:
        return jsonify({'message': "bad arguments"}), 400
    else:
        return jsonify({'message': "error"}), 500
