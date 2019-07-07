#!/bin/bash
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_pool
   Description :
   Author :       changfeng
   date：          2019/7/4
-------------------------------------------------
   Change Activity:
                   2019/7/4:
-------------------------------------------------
"""
__author__ = 'changfeng'

from multiprocessing import Process, Manager
import random
import time
import os

data = {}
def for_loop(msg):
    random.random() * 2
    time.sleep(random.random() *2)
    data[msg] = msg


def worker(msg, d):

    # 随机生成浮点数字。
    random.random() * 2
    time.sleep(random.random() * 2)

    d[msg] = msg


if __name__ == "__main__":

    # 创建一个进程池，里面最大包含三个三个进程。
    p_list = []  # 进程列表
    d = Manager().dict()
    starttime = time.time()
    for i in range(10):
        p = Process(target=worker, args=(i, d))  # 循环10次每次创建一个进程
        p.start()
        p_list.append(p)  # 加入进程列表里
    for res in p_list:  # 等所有进程结束
        res.join()
    endtime = time.time()
    print("time is ", endtime-starttime)
    print(d)

    starttime = time.time()
    for i in range(10):
        for_loop(i)
    endtime = time.time()

    print("start loop ", endtime-starttime)
    print(data)
