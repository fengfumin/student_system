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
from core import common_func
from interface import teacher_interface
from core import teacher as a

def login():
    '''
    老师登入
    :return:
    '''
    while True:
        name = input('请输入登入名(q退出)>>>:').strip()
        if name == 'q':
            return
        pwd = input('请输入登入密码>>>:').strip()
        if name and pwd:
            # 调用登入接口,拿到返回值
            obj, msg = teacher_interface.teacher_login(name, pwd)
            print(msg)
            if obj:
                global current_user
                current_user = obj
                return obj
        else:
            print('登入名或密码不能为空!')


@common_func.auth_login(a)
def check_course():
    '''
    老师查看学校课程
    :return:
    '''


@common_func.auth_login(a)
def choose_course():
    '''
    老师选择课程,关联到老师对象
    :return:
    '''
    

@common_func.auth_login(a)
def check_student():
    '''
    查看班级所有学生
    :return:
    '''


@common_func.auth_login(a)
def modify_score():
    '''
    添加学生成绩或修改成绩
    :return:
    '''

def teacher_view():
    '''
    管理员程序入口
    :return:
    '''
    funcs={'1':login,
           '2':check_course,
           '3':choose_course,
           '4':check_student,
           '5':modify_score,
                    }
    while True:
        print('''
1.老师登入
2.查看课程
3.选择课程
4.查看学生
5.修改成绩

        ''')
        while True:
            choose=input('请选择功能(q退出)>>>:').strip()
            if choose=='q':
                return
            if choose in funcs:
                funcs[choose]()
            else:
                print('输入错误!')