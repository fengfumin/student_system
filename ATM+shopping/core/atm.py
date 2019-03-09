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

from lib import common_user, bank
from lib import user

user_data = {'name': None}
user_shop = {'name': None}


def login():
    print('登入')
    count = 0
    while True:
        name = input('请输入登入账户名(q退出)>>>:').strip()
        if name == 'q': return
        pwd = input('请输入登入密码>>>:').strip()
        flag, msg = user.login(name, pwd)
        if flag:
            user_data['name'] = name
            user_shop['name'] = name
            print(msg)
            break
        else:
            print(msg)
            count += 1
            if count > 3:
                user.lock_user(name)
                print('尝试太多次输错，你已被锁定')
                break


@common_user.user_login_auth
def check_atm():
    print('查看余额，额度')
    balance, credit = bank.get_balance(user_data['name'])
    print('您的余额:%s 元,您的额度:%s' % (balance, credit))


@common_user.user_login_auth
def withdraw():
    print('取款')
    while True:
        account = input('请输入取款金额(q退出)>>>:').strip()
        if account == 'q': return
        if account.isdigit():
            account=int(account)
            flag, msg = bank.withdraw_lib(user_data['name'], account)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('金额必须是数字')


@common_user.user_login_auth
def transfer_account():
    print('转账')
    while True:
        to_name = input('请输入转账账户名(q退出)>>>:').strip()
        if to_name == 'q': return
        account = input('请输入转账金额>>>:').strip()
        if account.isdigit():
            account=int(account)
            flag, msg = bank.transfer_lib(user_data['name'], to_name, account)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('金额必须为数字')


@common_user.user_login_auth
def repayment():
    print('还款')
    while True:
        account = input('请输入还款金额(q退出)>>>:').strip()
        if account == 'q': return
        if account.isdigit():
            account=int(account)
            flag, msg = bank.repay_lib(user_data['name'], account)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('金额必须为数字')


@common_user.user_login_auth
def payment(cost):
    print('支付(购物系统调用)')
    flag, msg = bank.pay_lib(user_data['name'], cost)
    return flag, msg


@common_user.user_login_auth
def change_password():
    print('修改密码')
    while True:
        pwd = input('请输入你要修改的密码(q退出)>>>:').strip()
        if pwd == 'q': return
        conf_pwd = input('请再次确认密码>>>:').strip()
        if pwd == conf_pwd:
            flag, msg = bank.change_password_lib(user_data['name'], pwd)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码输入不一样')


@common_user.user_login_auth
def check_record():
    print('查看流水')
    bankflow = bank.check_record_lib(user_data['name'])
    for flow in bankflow:
        print(flow)


def atm_run():
    print('欢迎进入ATM系统')
    funcs = {
        '1': login,
        '2': check_atm,
        '3': withdraw,
        '4': transfer_account,
        '5': repayment,
        '6': change_password,
        '7': check_record

    }
    while True:
        print('''
1.登入
2.查看账户
3.取款
4.转账
5.还款
6.修改密码
7.查看流水
            ''')
        choise = input('请输入系统编码(q退出)>>>:').strip()
        if choise == 'q':
            print('你已退出系统')
            return
        if choise in funcs:
            funcs[choise]()
        else:
            print('输入错误！')
