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
import configparser
import json
import os
from conf import setting
import pickle


# 数据存储，用户信息，不包括管理员
def save_user(user_dic):
    # 获取用户信息文件的根目录（json格式文件）
    user_path = os.path.join(setting.BASE_DB, '%s.json' % user_dic['name'])
    # 创建一个用户信息文件，写入文件（json格式文件）
    with open(user_path, 'w', encoding='utf-8')as f:
        # json序列化用户信息写入文件
        json.dump(user_dic, f, ensure_ascii=False)
        f.flush()


# 获取登入用户信息
def select_user(name):
    # 获取用户信息文件的根目录（json格式文件）
    user_path = os.path.join(setting.BASE_DB, '%s.json' % name)
    # 如果文件存在则：读取
    if os.path.exists(user_path):
        with open(user_path, 'r', encoding='utf-8')as f:
            return json.load(f)
    else:
        return None


# 管理员登入读取
def admint_get():
    # 获取配置文件对象
    cfg = configparser.ConfigParser()
    # 配置读取文件路径
    cfg_path = os.path.join(setting.BASE_DB, 'admin.cfg')
    # 判断文件如果存在，读取
    if os.path.exists(cfg_path):
        cfg.read(cfg_path, encoding='utf-8')
        # 判断文件有内容读取
        if cfg.sections():
            name = cfg.get('admin', 'name')
            pwd = cfg.get('admin', 'pwd')
            if name == 'admin' and pwd == '123':
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# 管理员登入保存
def admin_save(admin_name, admin_pwd):
    # 获取配置文件对象
    cfg = configparser.ConfigParser()
    # 配置读取文件路径
    cfg_path = os.path.join(setting.BASE_DB, 'admin.cfg')
    # 读取文件
    cfg.read(cfg_path, encoding='utf-8')
    # 添加分区admin
    cfg.add_section('admin')
    # 添加选项和选项值
    cfg.set('admin', 'name', admin_name)
    cfg.set('admin', 'pwd', admin_pwd)
    # 写入cfg文件
    with open(cfg_path, "w", encoding="utf-8")as f:
        cfg.write(f)
        f.flush()


# 获取购物信息,在pickle文件内
def get_user_shop(name):
    shop_path = os.path.join(setting.BASE_DB, '%s.pickle' % name)
    if os.path.exists(shop_path):
        with open(shop_path, 'rb')as f:
            return pickle.load(f)
    else:
        return None


# 存储用户购物信息,存入pickle文件
def save_user_shop(user_shop):
    print(user_shop)
    shop_path = os.path.join(setting.BASE_DB, '%s.pickle' % user_shop['name'])
    with open(shop_path, 'wb')as f:
        pickle.dump(user_shop, f)
        f.flush()
