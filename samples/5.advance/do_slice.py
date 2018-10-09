#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 切片代码例子

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])  # 从左到右切片,下限索引从0开始编号
print('L[:3] =', L[:3])    # 下限索引值默认为0
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])  # 从右到左切片，下限索引从0开始编号

R = list(range(100))      # 返回一个list对象
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])
