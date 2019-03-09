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
from conf import setting
from db import models
import os


def admin_register(name,pwd):
    '''
    管理员注册接口
    :param name: 管理员用户名
    :param pwd: 管理员密码
    :return:
    '''
    obj=models.Admin.get_obj(name)
    if obj:
        return False,'该注册名已存在'
    models.Admin(name,pwd)
    return True,'注册成功'

def admin_login(name,pwd):
    '''
    管理员登入接口
    :param name: 管理员用户名
    :param pwd: 管理员密码
    :return: 管理员对象数据
    '''
    obj=models.Admin.get_obj(name)
    if obj:
        if obj.pwd==pwd:
            return obj,'登入成功'
        else:
            return False,'密码错误'
    else:
        return False,'用户名错误'

def create_school(school_name,school_addr):
    '''
    创建学校接口
    :param school_name: 学校名
    :param school_addr: 学校地址
    :return:
    '''
    school_obj=models.School.get_obj(school_name)
    if school_obj:
        return False,'该学校已存在'
    else:
        models.School(school_name,school_addr)
        return True,'创建<%s>校区成功'%school_name

def get_school_names():
    '''
    拿到所有的学校名字
    :return:
    '''
    school_path=os.path.join(setting.DB_DIR,'School')
    if os.path.exists(school_path):
        school_names=os.listdir(school_path)
        return True, school_names
    else:
        return False,'暂时还没有创建学校'

def get_school_obj(school_name):
    '''
    #拿到学校对象
    :param school_name: 学校名字
    :return:
    '''
    obj=models.School.get_obj(school_name)
    if obj:
        return True,obj
    else:
        return False,'学校不存在'

def create_course(course_name,course_price,course_period,school_obj):
    '''
    创建课程
    :param course_name: 课程名称
    :param course_price: 课程价格
    :param course_period: 课程周期
    :return:
    '''
    if course_name in [ c.name for c in school_obj.courses]:
        return False,'该课程已存在'
    else:
        obj=models.Course(course_name,course_price,course_period)
        school_obj.courses.append(obj)
        school_obj.save_obj()
        return True,'%s课程创建成功'%course_name

def create_teacher(teacher_name, teacher_gender, teacher_age,school_obj):
    '''
    创建老师
    :param teacher_name: 老师姓名
    :param teacher_gender: 性别
    :param teacher_age: 年龄
    :param school_obj: 学校对象
    :return:
    '''
    obj=models.Teacher.get_obj(teacher_name)
    if obj:
        return False,'该老师已存在'
    else:
        obj=models.Teacher(teacher_name,teacher_gender,teacher_age)
        school_obj.teachers.append(obj)
        school_obj.save_obj()
        return True,'%s老师创建成功'%teacher_name


def create_class(class_name,school_obj):
    '''
    创建班级
    :param class_name: 班级名
    :return:
    '''
    #先判断该学校有没有已存在该班级

    if class_name in [ c.name for c in school_obj.classes]:
        return False,'该班级名已存在'
    else:
        class_obj=models.Classes(class_name)
        school_obj.classes.append(class_obj)
        school_obj.save_obj()
        return True,'班级:%s 创建成功'%class_name

