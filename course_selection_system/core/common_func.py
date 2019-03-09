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
from interface import admin_interface


def choose_class(school_obj):
    '''
    选择班级.返回班级名称
    :param school_obj: 学校对象
    :return:
    '''
    #获取该学校的所有班级名称
    while True:
        class_names=[]
        if not school_obj.classes:
            return False,'暂时还没课程'
        for classes in school_obj.courses:
            class_names.append(classes.name)
        i = 0
        for name in class_names:
            print(str(i + 1) + ':' + name)
            i += 1
        num = input('请输入你要选择班级编码(q退出)>>>:').strip()
        if num == 'q':
            return False,'退出选择'
        num = int(num)
        if class_names[num - 1] in [name for name in class_names]:
            return True,class_names[num - 1]
        else:
           return False,'选择编码错误'


def choose_course(school_obj):
    '''
    选择课程名称,返回课程名字
    :param school_obj: 学校对象
    :return:
    '''
    #获取该学校的所有课程名称
    while True:
        course_names=[]
        if not school_obj.courses:
            return False,'暂时还没课程'
        for course in school_obj.courses:
            course_names.append(course.name)
        i = 0
        for name in course_names:
            print(str(i + 1) + ':' + name)
            i += 1
        num = input('请输入你要选择课程编码(q退出)>>>:').strip()
        if num == 'q':
            return False,'退出选择'
        num = int(num)
        if course_names[num - 1] in [name for name in course_names]:
            return True,course_names[num - 1]
        else:
           return False,'选择编码错误'





def choose_school_obj():
    '''
    选择学校,返回学校对象
    :return:
    '''
    state, school_names = admin_interface.get_school_names()
    while True:
        if state:
            i = 0
            for name in school_names:
                print(str(i + 1) + ':' + name)
                i += 1
            num = input('请输入你要选择学校编码(q退出)>>>:').strip()
            if num == 'q':
                return  False,'退出选择'
            num = int(num)
            if school_names[num - 1] in [name for name in school_names]:
                state, school_obj = admin_interface.get_school_obj(school_names[num - 1])
                return state,school_obj
            else:
                return False,'选择编码错误'
        else:
            return False,school_names

def auth_login(a):
    def outter(func):
        def wrapper(*args,**kwargs):
            if not a.current_user:
                print('请先登入')
                a.login()
                if a.current_user:
                    return func(*args,**kwargs)
            else:
                return func(*args,**kwargs)
        return wrapper
    return outter