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
from core import common_func
from core import admin as a

current_user = None


def register():
    """
    管理员注册功能
    :return:
    """
    while True:
        name = input('请输入注册名(q退出)>>>:').strip()
        if name == 'q':
            return
        pwd = input('请输入注册密码>>>:').strip()
        if name and pwd:
            # 调用注册接口,拿到返回值
            state, msg = admin_interface.admin_register(name, pwd)
            print(msg)
            if state:
                return
        else:
            print('注册名或密码不能为空!')


def login():
    '''
    管理员登入功能
    :return:
    '''
    while True:
        name = input('请输入登入名(q退出)>>>:').strip()
        if name == 'q':
            return
        pwd = input('请输入登入密码>>>:').strip()
        if name and pwd:
            # 调用登入接口,拿到返回值
            obj, msg = admin_interface.admin_login(name, pwd)
            print(msg)
            if obj:
                global current_user
                current_user = obj
                return obj
        else:
            print('登入名或密码不能为空!')

@common_func.auth_login(a)
def create_school():
    '''
    创建学校功能
    :return:
    '''
    while True:
        school_name = input('请输入学校名称(q退出)>>>:').strip()
        if school_name == 'q':
            return
        school_addr = input('请输入学校地址>>>:').strip()
        if school_name and school_addr:
            state, msg = admin_interface.create_school(school_name, school_addr)
            print(msg)
            if state:
                return
        else:
            print('学校名称和地址不能为空!')

@common_func.auth_login(a)
def create_course():
    '''
    创建课程功能
    :return:
    '''
    # 先拿到学校的所有名字
    state, school_obj = common_func.choose_school_obj()
    if state:
        while True:
            course_name = input('请输入要创建的课程名(q退出)>>>:').strip()
            if course_name == 'q':
                return
            course_price = input('请输入课程的价格>>>:').strip()
            course_period = input('请输入课程的周期>>>:').strip()
            if course_name and course_price and course_period:
                state, msg = admin_interface.create_course(course_name, course_price, course_period,school_obj)
                if state:
                    print(msg)
                    return
                else:
                    print(msg)
            else:
                print('输入内容不能为空')
    else:
        print(school_obj)


@common_func.auth_login(a)
def create_teacher():
    '''
    创建老师功能
    :return:
    '''
    # 先拿到学校的所有名字
    state,school_obj=common_func.choose_school_obj()
    if state:
        while True:
            teacher_name = input('请输入要创建的老师名(q退出)>>>:').strip()
            if teacher_name == 'q':
                return
            teacher_gender = input('请输入老师性别>>>:').strip()
            teacher_age = input('请输入老师年龄>>>:').strip()
            if teacher_name and teacher_gender and teacher_age:
                state, msg = admin_interface.create_teacher(teacher_name, teacher_gender, teacher_age,school_obj)
                if state:
                    print(msg)
                    return
                else:
                    print(msg)
            else:
                print('输入内容不能为空')
    else:
        print(school_obj)


@common_func.auth_login(a)
def create_class():
    '''
    创建班级功能
    :return:
    '''
    # 先拿到学校的所有名字
    state, school_obj = common_func.choose_school_obj()
    if state:
        #获取班级选择班级
        state,course_name=common_func.choose_course(school_obj)
        if state:
            while True:
                class_name = input('请输入要创建的班级名(q退出)>>>:').strip()
                if class_name == 'q':
                    return
                if class_name:
                    class_name=course_name+'<%s>'%class_name
                    state,msg=admin_interface.create_class(class_name,school_obj)
                    if state:
                        print(msg)
                        return
                    else:
                        print(msg)
                else:
                    print('班级名不能为空')
        else:
            print(course_name)
    else:
        print(school_obj)


def admin_view():
    '''
    管理员程序入口
    :return:
    '''
    funcs = {'1': register,
             '2': login,
             '3': create_school,
             '4': create_course,
             '5': create_teacher,
             '6': create_class
             }
    while True:
        print('欢迎进入管理员系统')
        print('''
1.管理员注册
2.管理员登入
3.创建学校
4.创建课程
5.创建老师
6.创建班级

        ''')
        choose = input('请选择功能(q退出)>>>:').strip()
        if choose == 'q':
            print('返回上一级菜单')
            global current_user
            current_user = None
            return
        if choose in funcs:
            funcs[choose]()
        else:
            print('输入错误!')


if __name__ == '__main__':

    pass

