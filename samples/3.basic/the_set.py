#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 列表转成集合,集合元素值不可以重复
s1 = set([1, 1, 2, 2, 3, 3, 5, '3'])
print(s1)
s2 = set([2, 3, 4, '5'])
print(s1 & s2)
print(s1 | s2)
