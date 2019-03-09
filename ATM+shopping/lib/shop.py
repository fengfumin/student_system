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

# 获取购物日志对象
sh_logger =common_logger .get_logger('shop')


# 查看购物车
def check_shoppingcart(name):
    user_shop = db_handler.get_user_shop(name)
    # sh_logger.info('%s查看了购物车'%name)
    return user_shop['shoppingcart']


# 获取购物车
def get_shopping_cart(name):
    user_shop = db_handler.get_user_shop(name)
    return user_shop['shoppingcart']


# 保存购物信息
def modfiy_shopping_cart(name, shoppingcart):
    user_shop = db_handler.get_user_shop(name)
    user_shop['shoppingcart'] = shoppingcart
    db_handler.save_user_shop(user_shop)
