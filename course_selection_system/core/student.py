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
from interface import student_interface
from core import student as a
from core import common_func

current_user=None
def register():
    '''
    学生注册
    :return:
    '''
    while True:
        name = input('请输入注册名(q退出)>>>:').strip()
        if name == 'q':
            return
        pwd = input('请输入注册密码>>>:').strip()
        gender=input('请输入性别>>>:').strip()
        age=input('请输入年龄>>>:').strip()
        if not age.isupper():
            print('年龄必须是数字')
            continue
        if name and pwd and gender and age:
            # 调用登入接口,拿到返回值
            obj, msg = student_interface.student_register(name,pwd,gender,age)
            print(msg)
            if obj:
                return
        else:
            print('输入内容不能为空!')

def login():
    '''
    学生登入
    :return:
    '''
    while True:
        name = input('请输入登入名(q退出)>>>:').strip()
        if name == 'q':
            return
        pwd = input('请输入登入密码>>>:').strip()
        if name and pwd:
            # 调用登入接口,拿到返回值
            obj, msg = student_interface.student_login(name, pwd)
            print(msg)
            if obj:
                global current_user
                current_user = obj
                return obj
        else:
            print('登入名或密码不能为空!')

@common_func.auth_login(a)
def choose_school():
    '''
    学生选择校区
    :return:
    '''
    while True:
        state,school_obj=common_func.choose_school_obj()
        if state:
            state,msg=student_interface.student_choose_school(school_obj,current_user)
            if state:
                print(msg)
                return
            else:
                print(msg)


@common_func.auth_login(a)
def choose_course():
    '''
    学生选择课程
    :return:
    '''
    #查看已选择的校区有哪些课程

    if current_user.school_name:
        print('你还没选择校区')
        return
    # 1.先拿到学校对象,查看学校下有哪些课程
    school_obj=student_interface.student_get_school_obj(current_user.school_name)
    state,course_name=common_func.choose_course(school_obj)
    if state:
        #把选择好的课程关联到学生对象
        state=student_interface.student_choose_course(course_name,current_user,school_obj)
        print(state)
        return
    else:
        print(course_name)

@common_func.auth_login(a)
def choose_class():
    '''
    学生选择班级
    :return:
    '''
    if current_user.school_name:
        print('你还没选择校区')
        return
    #查看该学生选择的校区有哪些班级
    school_obj = student_interface.student_get_school_obj(current_user.school_name)
    state,class_name=common_func.choose_class(school_obj)
    if state:
        #把选择好的班级关联到学生对象
        state = student_interface.student_choose_class(class_name, current_user, school_obj)
        print(state)
        return
    else:
        print(class_name)

@common_func.auth_login(a)
def check_score():
    '''
    学生查看成绩
    :return:
    '''


def student_view():
    '''
    管理员程序入口
    :return:
    '''
    funcs={'1':register,
           '2':login,
           '3':choose_school,
           '4':choose_course,
           '5':choose_class,
           '6':check_score
                    }
    while True:
        print('''
1.学生注册
2.学生登入
3.学生选课

        ''')
        while True:
            choose=input('请选择功能(q退出)>>>:').strip()
            if choose=='q':
                return
            if choose in funcs:
                funcs[choose]()
            else:
                print('输入错误!')