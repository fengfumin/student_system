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
from core import admin, atm, shopping


def system_run():
    print('欢迎进入ATM+购物系统')
    funcs = {'1': admin.admin_run,
             '2': atm.atm_run,
             '3': shopping.shopping_run}
    while True:
        print('''
1.系统管理员
2.ATM系统
3.购物系统
        ''')
        choise = input('请输入系统编码(q退出)>>>:').strip()
        if choise == 'q':
            print('你已退出系统')
            return
        if choise in funcs:
            funcs[choise]()
        else:
            print('输入错误！')
