#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025.07.25 
# @Author : 王沁桐(3636617336@qq.com)
# @File : main.py
# @Description : 

import sys

from db_connection import create_db_connection
from query import (query_by_name,query_by_department,query_by_min_salary)
from result_display import display_results

def main():
    """
    主函数
    """
    if len(sys.argv) < 3:
        print("  按名字查询: python main.py name <first_name> (例如: python main.py name Gor)")
        print("  按部门查询: python main.py dept '<dept_name>' (例如: python main.py dept 'Sales')")
        print("  按最低工资查询: python main.py salary <min_salary> (例如: python main.py salary 100000)")
        return
   
    query_value = sys.argv[2]
    query_type = sys.argv[1]
    query_value = sys.argv[2]
    
    conn = create_db_connection()
    
    try:
        if query_type == "name":
            result = query_by_name(conn, query_value)
        elif query_type == "dept":
            result = query_by_department(conn, query_value)
        elif query_type == "salary":
            try:
                min_salary = int(query_value)
                result = query_by_min_salary(conn, min_salary)
            except ValueError:
                print("错误：工资必须是数字")
                return
        display_results(result)
    finally:
        if conn:
            conn.close()
            print ("数据库连接已关闭。")        

if __name__ == "__main__":
    main()

