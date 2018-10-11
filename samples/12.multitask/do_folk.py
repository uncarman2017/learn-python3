#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# fork() 方法在Linux/Unix/Mac环境下有效,会返回两次，创建一个父进程和一个子进程(父进程的拷贝)


import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
