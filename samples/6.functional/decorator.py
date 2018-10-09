#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 装饰器示例

import functools


def log(func):
    @functools.wraps(func)   # 似乎不使用这个装饰器也可以
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper    # 装饰器方法需要返回方法本身


@log
def now():
    print('2015-3-25')


now()

# 多层装饰器用法


def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@logger('DEBUG')
def today():
    print('2015-3-25')


today()
print(today.__name__)
