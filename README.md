# 员工信息查询系统

A Python-based tool to query employee information from a MySQL database, supporting multi-condition filtering (by name, department, or minimum salary).

## 项目简介

该系统用于从 `employees` MySQL 数据库中查询员工信息，支持三种查询模式：按姓名、按部门名称、按最低工资，返回员工编号、姓名、部门、职位、薪资等关键信息。

## 核心功能

- 连接 MySQL 数据库并验证连接有效性
- 支持三种查询模式：
  - 按员工姓名查询（精确匹配）
  - 按部门名称查询（支持含空格的部门名，如 `"Senior Management"`）
  - 按最低工资查询（返回薪资不低于指定值的员工）
- 格式化展示查询结果，无匹配时提示明确信息
- 自动处理数据库连接的创建与关闭，确保资源释放

## 环境要求

- **Python 版本**：3.5 及以上
- **数据库**：MySQL 5.7 及以上（需预先创建 `employees` 数据库及关联表，表结构需包含 `employees`、`dept_emp`、`titles`、`salaries`、`departments`）
- **依赖库**：`pymysql`（版本 `1.1.0`，见 `requirements.txt`）

## 安装步骤

### 1. 获取项目代码

bash

```bash
# 克隆仓库（若使用版本控制）
git clone <https://github.com/haodehaode378/querySQL>
cd employee-query-system  # 进入项目目录
```

### 2. 安装依赖

bash

```bash
pip install -r requirements.txt
```

## 数据库配置

1. 确保 MySQL 服务已启动，且 `employees` 数据库存在。

2. 修改

   ```
   config.py
   ```

   

   配置文件，适配你的数据库环境：

   python

   ```python
   # config.py
   db_config = {
       "host": "localhost",      # 数据库地址（默认 localhost）
       "port": 3306,             # 端口（默认 3306）
       "user": "root",           # 数据库用户名
       "password": "123456",     # 替换为你的数据库密码
       "database": "employees",  # 数据库名（固定为 employees）
       "autocommit": True
   }
   ```

## 使用指南

### 基本语法

在终端中执行以下命令，根据查询类型传递参数：

bash

```bash
python main.py <查询类型> <查询值>
```

### 三种查询模式示例

#### 1. 按姓名查询

bash

```bash
# 查询名为 "Gor" 的员工
python main.py name Gor
```

#### 2. 按部门查询

- 若部门名称含空格（如

  ```
  Customer Service
  ```

  ），需用引号包裹：

  bash

  ```bash
  # 查询部门为 "Customer Service" 的员工
  python main.py dept "Customer Service"
  ```

- 部门名称无空格时直接传递：

  bash

  ```bash
  # 查询部门为 "Sales" 的员工
  python main.py dept Sales
  ```

#### 3. 按最低工资查询

bash

```bash
# 查询薪资不低于 100000 的员工
python main.py salary 100000
```

### 输出说明

- 若存在匹配结果，将显示：

  plaintext

  ```plaintext
  查询结果:
  (10001, 'Gor', 'Smith', 'd001', 'Marketing', 'Senior Engineer', 120000)
  (10005, 'Gor', 'Williams', 'd003', 'Human Resources', 'Staff', 110000)
  ```

- 若无匹配记录，将提示：

  plaintext

  ```plaintext
  没有找到匹配的记录。
  ```

## 项目结构

plaintext

```plaintext
employee-query-system/
├── config.py               # 数据库配置（主机、端口、账号密码等）
├── db_connection.py        # 数据库连接工具（创建连接、错误处理）
├── query.py                # 核心查询逻辑（三种查询的SQL语句与执行）
├── result_display.py       # 结果展示模块（格式化输出查询结果）
├── main.py                 # 主程序入口（解析参数、调用模块、协调流程）
├── requirements.txt        # 依赖清单（pymysql==1.1.0）
└── README.md               # 项目说明文档（本文件）
```

## 注意事项

1. **参数传递**：
   - 部门名称含空格时，必须用双引号 `"` 或单引号 `'` 包裹（如 `python main.py dept "Research and Development"`），否则会被识别为多个参数。
   - 薪资参数必须是整数（如 `100000`），输入非数字会提示错误。
2. **查询条件**：
   - 所有查询默认只返回 **在职员工**（`to_date='9999-01-01'`），如需调整，可修改 `query.py` 中的 SQL 语句。
   - 姓名和部门名称匹配对大小写敏感（与数据库存储一致）。
3. **数据依赖**：
   - 确保 `employees` 数据库中已创建关联表（`employees`、`dept_emp`、`titles`、`salaries`、`departments`），且表结构包含必要字段（如 `emp_no`、`dept_name`、`salary` 等）。

## 许可证

[MIT](https://opensource.org/licenses/MIT)
允许自由使用、修改和分发，需保留原作者信息。

## 联系方式

- 作者：王沁桐
- 邮箱：3636617336@qq.com