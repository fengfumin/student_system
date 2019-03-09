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
import os

# 获取项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# print(BASE_DIR)
# 获取db文件夹目录
BASE_DB = os.path.join(BASE_DIR, 'db')
# print(BASE_DB)
# 获取log文件夹目录
BASE_LOG = os.path.join(BASE_DIR, 'log')

# 设置日志输出格式：打印到文件内的
standard_format = '%(asctime)s-%(threadName)s-%(thread)d-task_id:%(name)s-%(filename)s-%(lineno)d-' \
                  '%(levelname)s:[%(message)s]'
# 设置日志输出格式：打印到终端
simple_format = '%(levelname)s-%(asctime)s-%(filename)s-%(lineno)d-%(message)s'

id_simple_format = '%(levelname)s-%(asctime)s- %(message)s'

# 如果日志写入文件目录不存在，就创建一个文件目录
if not os.path.isdir(BASE_LOG):
    os.mkdir(BASE_LOG)

# 日志文件log的全路径
logfile_path = os.path.join(BASE_LOG, 'log.log')

# ？是否会自动创建log文件

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024 * 5 * 1024,  # 日志大小 5M
            'backupCount': 5,
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },

    },
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'INFO',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}
