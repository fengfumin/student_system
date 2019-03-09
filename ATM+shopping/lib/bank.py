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
from db import db_handler
from lib import common_logger

bank_logger= common_logger.get_logger('bank')




# 获取账户名信息的金额,和额度
def get_balance(name):
    # 获取登入账户信息
    user_dic = db_handler.select_user(name)
    return user_dic['balance'], user_dic['credit']


# 转账
def transfer_lib(from_name, to_name, account):
    if from_name == to_name:
        return False, '不能给自己转账'
    to_dic = db_handler.select_user(to_name)
    if to_dic:
        from_dic = db_handler.select_user(from_name)
        if account > from_dic['balance']:
            return False, '你的余额不足'
        else:
            from_dic['balance'] -= account
            from_dic['bankflow'].append('您向%s转账%s元' % (to_dic['name'], account))
            to_dic['balance'] += account
            to_dic['bankflow'].append('您收到%s转账%s元' % (from_dic['name'], account))
            db_handler.save_user(from_dic)
            db_handler.save_user(to_dic)
            bank_logger.info('向%s转账%s元' % (to_dic['name'], account))
            return True, '转账成功'
    else:
        return False, '对方账户不存在'


# 取款
def withdraw_lib(name, account):
    user_dic = db_handler.select_user(name)
    if user_dic['balance'] > account:
        user_dic['balance'] -= account
        user_dic['bankflow'].append('%s取款:%s' % (name, account))
        db_handler.save_user(user_dic)
        bank_logger().info('取款:%s' % account)
        return True, '取款功能'
    else:
        return False, '您的余额不足'


# 还款
def repay_lib(name, account):
    user_dic = db_handler.select_user(name)
    user_dic['balance'] += account
    user_dic['bankflow'].append('%s还款%s元' % (name, account))
    db_handler.save_user(user_dic)
    bank_logger.info('%s还款%s元' % (name, account))
    return True, '还款成功'


# 支付
def pay_lib(name, cost):
    user_dic = db_handler.select_user(name)
    if user_dic['balance'] > cost:
        user_dic['balance'] -= cost
        user_dic['bankflow'].append('%s购物支付了%s' % (name, cost))
        db_handler.save_user(user_dic)
        bank_logger.info('%s购物支付了%s' % (name, cost))
        return True, '支付成功'
    else:
        return False, '余额不足'


# 查看流水
def check_record_lib(name):
    user_dic = db_handler.select_user(name)
    return user_dic['bankflow']


# 修改密码
def change_password_lib(name, pwd):
    user_dic = db_handler.select_user(name)
    user_dic['password'] = pwd
    db_handler.save_user(user_dic)
    return True, '密码修改成功'
