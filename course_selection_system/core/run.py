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
from core import admin ,student ,teacher


def run():
    '''
    主程序入口
    :return:
    '''
    funcs={'1':admin.admin_view,
           '2':student.student_view,
           '3':teacher.teacher_view}
    while True:
        print('欢迎进入选课系统')
        print('''
1.管理员系统
2.学生系统
3.老师系统
        ''')
        choose=input('请选择功能(q退出)>>>:').strip()
        if choose=='q':
            print('再见!')
            return
        if choose in funcs:
            funcs[choose]()
        else:
            print('输入错误!')
