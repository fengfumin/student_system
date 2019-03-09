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
class BaseClass:

    @classmethod
    def get_obj(cls,name):
        return db_handler.get_obj(cls.__name__,name)

    def save_obj(self):
        return db_handler.save_obj(self)


class Admin(BaseClass):
    def __init__(self,name,pwd):
        self.name=name
        self.pwd=pwd
        #自动保存,对象自己创建时自己调用父类的save_obj()
        self.save_obj()

class School(BaseClass):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.courses=[]
        self.teachers=[]
        self.classes=[]
        self.save_obj()

    def __str__(self):
        return '学校名称:%s 学校地址:%s'%(self.name,self.addr)

class Course(BaseClass):
    def __init__(self,name,price,period):
        self.name=name
        self.price=price
        self.period=period


    def __str__(self):
        return '课程:%s 价格:%s 周期:%s'%(self.name,self.price,self.period)

class Teacher(BaseClass):
    def __init__(self,name,gender,age):
        self.name=name
        self.pwd='123'
        self.gender=gender
        self.age=age
        self.save_obj()

    #添加学生成绩
    def add_score(self):
        pass

    #修改学生成绩
    def modife_score(self):
        pass

    def __str__(self):
        return '老师:%s 性别:%s 年龄:%s'%(self.name,self.gender,self.age)

class Student(BaseClass):
    def __init__(self,name,pwd,gender,age):
        self.name=name
        self.pwd=pwd
        self.gender=gender
        self.age=age
        self.school_name = None
        self.courses = []
        self.classes=[]
        self.scores={}
        self.save_obj()

    def __str__(self):
        return '学生:%s 性别:%s 年龄:%s'%(self.name,self.gender,self.age)

class Classes(BaseClass):
    def __init__(self,name):
        self.name=name
        self.student=[]
        self.save_obj()

    def __str__(self):
        return '班级:%s'%self.name




