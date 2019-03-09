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

def student_register(name, pwd,gender,age):
    '''
    学生注册
    :param name: 名字
    :param pwd: 密码
    :param gender: 性别
    :param age: 年龄
    :return:
    '''
    obj=models.Student.get_obj(name)
    if obj:
        return False,'该学生姓名已存在'
    else:
        obj=models.Student(name,pwd,gender,age)
        return True,'学生:%s注册成功'%name

def student_login(name, pwd):
    '''
    学生登入
    :param name: 名字
    :param pwd: 密码
    :return:
    '''
    obj=models.Student.get_obj(name)
    if obj:
        if obj.pwd==pwd:
            return obj,'登入成功'
        else:
            return False,'密码错误'
    else:
        return False,'登入名错误'

def student_choose_school(school_obj,current_user):
    '''
    学生选择校区
    :param school_obj: 学校对象
    :return:
    '''
    if current_user.school_name:
        return False,'你已经是<%s>校区学生'%current_user.school_name
    else:
        current_user.school_name=school_obj.name
        current_user.save_obj()
        return True,'你成功选择了<%s>校区'%school_obj.name

def student_get_school_obj(school_name):
    '''
    拿到登入学生的学校对象
    :param school_name: 学校名字
    :return:
    '''

    school_obj=models.School.get_obj(school_name)
    return school_obj

def student_choose_course(course_name,current_user,school_obj):
    '''
    登入学生选择课程,将课程对象关联到学生
    :param course_name: 课程名字
    :param current_user: 登入学生对象
    :return:
    '''
    for course_obj in school_obj.courses:
        if course_obj.name==course_name:
            current_user.courses.append(course_obj)
            current_user.save_obj()
            return '选择课程<%s>成功'%course_name

def student_choose_class(class_name, current_user, school_obj):
    '''
    登入学生选择班级,将课程对象关联到学生
    :param class_name: 班级名
    :param current_user: 登入学生对象
    :param school_obj: 学校对象
    :return:
    '''
    for class_obj in school_obj.classes:
        if class_obj.name==class_name:
            current_user.classes.append(class_obj)
            current_user.save_obj()
            class_obj.student.append(current_user)
            class_obj.save_obj()
            return '选择班级<%s>成功'%class_name


