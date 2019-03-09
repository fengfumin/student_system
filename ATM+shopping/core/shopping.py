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
from lib import bank, shop,common_user
from core import atm


user_shop = atm.user_shop

@common_user.user_login_auth
def shopping_center():
    print('欢迎来购物中心')
    '''
    1.先循环打印商品
    2.用户输入数字选择商品（判断是否是数字，判断输入的数字是否在范围）
    3.取出商品名称，商品价额
    4.判断用户余额是否大于商品总价格
    5.余额大于商品总价时，判断此商品是否在购物车
    6.用户余额减掉商品价格
    7.花费加上商品总价格
    :return:
    '''
    print('购物')
    goods_list = [
        ['苹果电脑', 10000],
        ['苹果手机', 8000],
        ['苹果pid', 5000],
        ['苹果手表', 3000],
        ['苹果手机', 8000],
    ]
    user_balance,x = bank.get_balance(user_shop['name'])
    cost = 0
    shoppingcart = shop.get_shopping_cart(user_shop['name'])

    while True:
        # 将[(0:['苹果电脑',10000]),(1:['苹果手机',8000])...]组成元组形式的列表做循环
        for i, goods in enumerate(goods_list):  # enumerate将值和索引组成一个元组
            na, pr = goods
            print('编号：%s，名称：%s，价格：%s' % (i, na, pr))
        buy = input('请输入要购买的商品编码(q退出)>>>:').strip()
        if buy.isdigit():
            buy = int(buy)
            if buy >= len(goods_list):
                print('商品编码不存在')
                continue
            buy_count = input('请输入选购商品的数量>>>:').strip()
            if '1' >= buy_count > '10':
                print('最大数量不能大于10个')
                continue
            if buy_count.isdigit():
                buy_count = int(buy_count)
                goods_name = goods_list[buy][0]
                goods_price = goods_list[buy][1]
                if user_balance >= goods_price * buy_count:
                    # 判断购物车中是否已有选购商品
                    if goods_name in shoppingcart:
                        # 有商品就累计上去商品次数
                        shoppingcart[goods_name]['count'] += buy_count
                    else:
                        # 添加购物商品信息到购物车字典中
                        shoppingcart[goods_name] = {'price': goods_price, 'count': buy_count}
                    # 把账户金额减去商品总价
                    user_balance -= goods_price * buy_count
                    # 把总价格加入到cost，等待支付
                    cost += goods_price * buy_count
                    # 将购物商品信息保存到json文件中
                    # sopping_car中的数据添加到shoppingcarts中
                    shop.modfiy_shopping_cart(user_shop['name'], shoppingcart)
                else:
                    print('余额不足')
                    return
            else:
                print('选购数量必须为数字')
        elif buy == 'q':
            if cost == 0: break
            print(shoppingcart)
            confim = input('确认购买？y/n').strip()
            if confim == 'y':
                flag, msg = atm.payment( cost)
                if flag:
                    print(msg)
                    return
                else:
                    print(msg)
            else:
                print('什么也没买')
                return
        else:
            print('编码输入错误')

@common_user.user_login_auth
def check_shop():
    print('查看所有已购物商品')
    shoppingcart = shop.get_shopping_cart(user_shop['name'])
    if shoppingcart:
        print(shoppingcart)


def shopping_run():
    print('欢迎进入购物中心系统')
    funcs = {
        '1': shopping_center,
        '2': check_shop
    }
    while True:
        print('''
        1.购物中心
        2.查看所有已购物商品
            ''')
        choise = input('请输入系统编码(q退出)>>>:').strip()
        if choise == 'q':
            print('你已退出系统')
            return
        if choise in funcs:
            funcs[choise]()
        else:
            print('输入错误！')
