#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2025.07.25
# @Author : 王沁桐(3636617336@qq.com)
# @File : db_connection.py
# @Description : 

from pymysql import Connection,OperationalError
from config import db_config

def create_db_connection():
    """
    创建数据库连接
    :return: 数据库连接对象
    """

    try:
        conn = Connection(**db_config)
        return conn
    except OperationalError as e:
        return None