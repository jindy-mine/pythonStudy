"""
=========================================
Author:薄咊
Time:2020/3/25  23:37
==========================================
"""
import os, datetime

# 获取项目所在的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 用例模块所在的目录路径
CASE_DIR = os.path.join(BASE_DIR, "testcases")
# 测试报告所在的目录路径
s = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
REPORT_FILENAME = os.path.join(REPORT_DIR, "report.html")
