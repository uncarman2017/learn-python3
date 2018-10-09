#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# map函数返回的是一个iterator（惰性队列）


def f(x):
    return x * x


print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
