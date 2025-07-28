#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025.07.25 
# @Author : 王沁桐(3636617336@qq.com)
# @File : query.py
# @Description : 

from pymysql import ProgrammingError

def query_by_name(conn, first_name):
    """
    查询员工信息
    :param conn: 数据库连接对象
    :param first_name: 员工名
    :return: 查询结果
    """
    
    sql = """
    SELECT e.emp_no, e.first_name, e.last_name, de.dept_no, d.dept_name, t.title, s.salary
    FROM employees e
    JOIN dept_emp de ON e.emp_no = de.emp_no
    JOIN titles t ON e.emp_no = t.emp_no
    JOIN salaries s ON e.emp_no = s.emp_no
    JOIN departments d ON d.dept_no = de.dept_no
    WHERE e.first_name = %s
      AND s.to_date = '9999-01-01'
      AND t.to_date = '9999-01-01'
      AND de.to_date = '9999-01-01'
    """
    return _execute_sql(conn, sql, (first_name))

def query_by_department(conn, dept_name):
    """
    查询指定部门下的员工信息
    参数：
    :param conn: 数据库连接对象
    :param ept_name: 部门名称
    :return: 查询结果
    """
    
    sql = """
    SELECT e.emp_no, e.first_name, e.last_name, d.dept_name, t.title, s.salary
    FROM employees e
    JOIN dept_emp de ON e.emp_no = de.emp_no
    JOIN departments d ON de.dept_no = d.dept_no
    JOIN salaries s ON e.emp_no = s.emp_no
    JOIN titles t ON e.emp_no = t.emp_no
    WHERE d.dept_name = %s
      AND de.to_date = '9999-01-01'
      AND t.to_date = '9999-01-01'
      AND s.to_date = '9999-01-01'
    """
    return _execute_sql(conn, sql, (dept_name))

def query_by_min_salary(conn, min_salary):
    """
    查询员工信息，根据最低工资
    :param conn: 数据库连接对象
    :param min_salary: 最低工资
    :return: 查询结果
    """
    
    sql = """
    SELECT e.emp_no, e.first_name, e.last_name, d.dept_name, t.title,
    s.salary
    FROM employees e
    JOIN salaries s ON e.emp_no = s.emp_no
    JOIN dept_emp de ON e.emp_no = de.emp_no
    JOIN departments d ON de.dept_no = d.dept_no
    JOIN titles t ON e.emp_no = t.emp_no
    WHERE s.salary >= %s
      AND de.to_date = '9999-01-01'
      AND t.to_date = '9999-01-01'
      AND s.to_date = '9999-01-01'
    """
    return _execute_sql(conn, sql, (min_salary))

def _execute_sql(conn, sql, params):
    """
    执行SQL语句
    :param conn: 数据库连接对象
    :param sql: SQL语句
    :param params: 参数列表
    :return: 查询结果
    """
    
    cursor = conn.cursor()
    try:
        cursor.execute(sql, params)
        return cursor.fetchall()
    except ProgrammingError as e:
        print (f"SQL执行错误: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        
        