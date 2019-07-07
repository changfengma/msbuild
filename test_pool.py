#!/bin/bash
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_pool
   Description :
   Author :       changfeng
   date：          2019/7/7
-------------------------------------------------
   Change Activity:
                   2019/7/7:
-------------------------------------------------
"""
__author__ = 'changfeng'

import time
import multiprocessing
from multiprocessing import cpu_count


def much_job(x):
    time.sleep(5)
    return x ** 2


# 串行任务
def test_serial():

    ans = [much_job(i) for i in range(8)]
    print(ans)


# 测试多进程(进程池)
def test_paral():
    # 多进程任务
    pool = multiprocessing.Pool(processes=cpu_count())
    result = []
    for i in range(8):
        result.append(pool.apply_async(func=much_job, args=(i,)))
    pool.close()
    pool.join()

    ans = [res.get() for res in result]
    print(ans)


if __name__ == "__main__":
    start = time.time()
    test_serial()
    print("test_serial spend time is %s" % (str(time.time() - start)))

    start = time.time()
    test_paral()
    print("test_paral spend time is %s" % (str(time.time() - start)))
