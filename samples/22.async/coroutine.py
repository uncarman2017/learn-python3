#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。


def consumer():
    r = ''
    while True:
        n = yield r  # consumer程序通过yield取得传递过来的数据,Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'   # 通过yield把结果传回


def produce(c):
    c.send(None)   # 启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)   # 获取consumer的返回数据
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()  # 关闭consumer，不再生产消息


c = consumer()
produce(c)
