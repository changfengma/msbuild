#!/bin/bash
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :       changfeng
   date：          2019/6/28
-------------------------------------------------
   Change Activity:
                   2019/6/28:
-------------------------------------------------
"""
__author__ = 'changfeng'


import os

def test_subprocess_popen(cmd):
    import subprocess
    a = subprocess.getoutput(cmd)
    
    print(a)
    print(type(a))



def main():
    string = r"C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe  E:\cprogram\cmake_test\test1\HELLO.sln /property:Configuration=Release /t:build /p:VisualStudioVersion=12.0"
    
    # os.system(string)
    test_subprocess_popen(string)

if __name__ == "__main__":
    main()
