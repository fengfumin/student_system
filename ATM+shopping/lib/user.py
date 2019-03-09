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

from db import db_handler
from lib import common_logger

user_logger = common_logger.get_logger('user')


# 后台注册ATM账户
def register_lib(name, password):
    user_dic = db_handler.select_user(name)
    if user_dic:
        return False, '账户已存在'
    else:
        user_dic = {'name': name, 'password': password,
                    'locked': False, 'balance': 2000, 'credit': 2000, 'bankflow': []}
        db_handler.save_user(user_dic)
        user_shop = {'name': name, 'shoppingcart': {}}
        db_handler.save_user_shop(user_shop)
        user_logger.info('%s注册成功' % name)
        return True, '注册成功'


# 后台ATM账户登入
def login(name, password):
    user_dic = db_handler.select_user(name)
    if user_dic:
        if user_dic['password'] == password:
            return True, '登入成功'
        else:
            return False, '密码错误'
    else:
        return False, '账户名错误'


# 后台ATM账户锁定
def lock_user(name):
    user_dic = db_handler.select_user(name)
    user_dic['locked'] = True
    db_handler.save_user(user_dic)
