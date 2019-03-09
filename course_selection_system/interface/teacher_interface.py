# -*- coding: utf-8 -*-
"""
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""

from db import models

def teacher_login(name, pwd):
    '''
    老师登入
    :param name: 名字
    :param pwd: 密码
    :return:
    '''
    obj=models.Teacher.get_obj(name)
    if obj:
        if obj.pwd==pwd:
            return True,obj
        else:
            return False,'密码错误'
    else:
        return False,'登入名错误'


