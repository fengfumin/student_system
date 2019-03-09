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
import os
import pickle
from conf import setting

def get_obj(cls_name,obj_name):
    path=os.path.join(setting.DB_DIR,cls_name,obj_name)
    if os.path.exists(path):
        with open(path,'rb')as f:
            obj=pickle.load(f)
        return obj
    return

def save_obj(obj):

    path=os.path.join(setting.DB_DIR,obj.__class__.__name__)
    if not os.path.exists(path):
        os.mkdir(path)
    obj_path=os.path.join(path,obj.name)
    with open(obj_path,'wb')as f:
        pickle.dump(obj,f)
        f.flush()


