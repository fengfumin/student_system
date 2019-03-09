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
import re
from lib import common_admin, user
from db import db_handler


def admin_login():
    print('管理员登入')
    # 获取cfg文件读取结果
    flag = db_handler.admint_get()
    # 结果为True，则说明cfg文件内又存用户名和密码
    if flag:
        print('已配置账户密码，登入成功')
        return
    else:
        while True:
            admin_name = input('请输入管理员账户(q退出)>>>:').strip()
            if admin_name == 'q': return
            if not admin_name:
                print('账户不能为空')
                continue
            admin_pwd = input('请输入管理员密码>>>:').strip()
            if admin_pwd.isdigit():
                if admin_name == 'admin' and admin_pwd == '123':
                    print('管理员登入成功')
                    if input("需要记住密码吗? y/n") == "y":
                        db_handler.admin_save(admin_name, admin_pwd)
                        print('记录成功')
                        return
                    else:
                        return
                else:
                    print('账户名或密码错误')
            else:
                print('密码为纯数字')


@common_admin.admin_login_auth
def add_account():
    print('添加账户')
    while True:
        user_name = input('请输入注册账户名(q退出)>>>:').strip()
        if user_name == 'q': return
        if not re.search('^.{3,}$', user_name):
            print('账户名不能少于3位！')
            continue
        user_pwd = input('请输入注册密码>>>:').strip()
        if user_pwd.isdigit():
            flag, msg = user.register_lib(user_name, user_pwd)
            if flag:
                print(msg)
                return
            else:
                print(msg)
                return
        else:
            print('密码必须为纯数字')


@common_admin.admin_login_auth
def lock():
    print('锁定账户')
    name = input('请输入你要锁定的账户名(q退出)>>>:').strip()
    if name == 'q': return
    user_dic = db_handler.select_user(name)
    if user_dic:
        if user_dic['locked'] == True:
            print('该账户已经锁定')
            return
        else:
            user_dic['locked'] = True
            db_handler.save_user(user_dic)
            print('该账户锁定成功')
            return
    else:
        print('账户名不存在')


@common_admin.admin_login_auth
def unlock():
    print('解锁账户')
    name = input('请输入你要解锁的账户名(q退出)>>>:').strip()
    if name == 'q': return
    user_dic = db_handler.select_user(name)
    if user_dic:
        if user_dic['locked'] == False:
            print('该账户已经解锁')
            return
        else:
            user_dic['locked'] = False
            db_handler.save_user(user_dic)
            print('该账户解锁成功')
            return
    else:
        print('账户名不存在')


@common_admin.admin_login_auth
def check_account():
    print('查看账户')
    name = input('请输入你要查看的账户名(q退出)>>>:').strip()
    if name == 'q': return
    user_dic = db_handler.select_user(name)
    if user_dic:
        print(user_dic)
        return
    else:
        print('账户名不存在')


def admin_run():
    print('欢迎进入管理员系统')
    funcs = {
        '1': admin_login,
        '2': add_account,
        '3': lock,
        '4': unlock,
        '5': check_account
    }

    while True:
        print('''
1.管理员登入
2.添加账户
3.锁定账户
4.解锁账户
5.查看账户
            ''')
        choise = input('请输入系统编码(q退出)>>>:').strip()
        if choise == 'q':
            print('你已退出系统')
            return
        if choise in funcs:
            funcs[choise]()
        else:
            print('输入错误！')
