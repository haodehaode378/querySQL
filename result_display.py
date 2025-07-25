#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025.07.25 
# @Author : 王沁桐(3636617336@qq.com)
# @File : result_display.py
# @Description : 

def display_results(results):
    """
    显示查询结果
    :param results: 查询结果
    """
    
    if results:
        print("查询结果:")
        for row in results:
            print(row)
    else:
        print("没有找到匹配的记录。")