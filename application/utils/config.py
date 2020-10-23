# -*- coding: utf-8 -*-
import os
import yaml

basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

with open(os.path.join(basedir, 'config.yaml')) as f:
    settings = yaml.load(f.read())


def get_yaml(key, default=None):
    data = settings
    for i in key.split('.'):
        data = data.get(i, default)
    return data


def get_env(key, default, vtype=str):
    """
    通过环境变量获取值
    :param key:
    :param default:
    :param vtype:
    :return:
    """
    result = os.getenv(key, default)
    if vtype == int:
        return int(result)
    elif vtype == bool:
        return result == str(True)
    elif vtype == dict:
        return result
    elif vtype == str:
        return result


if __name__ == '__main__':
    print(settings)