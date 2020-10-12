"""
=========================================
Author:薄咊
Time:2020/9/30  23:55
comments:python学习
==========================================
"""
import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner
from common.handle_path import REPORT_FILENAME,CASE_DIR


# 创建测试套件
suite = unittest.TestSuite()

# 加载用例到套件
loader = unittest.TestLoader()
# 执行所有测试用例类
suite.addTest(loader.discover(CASE_DIR))

runner = HTMLTestRunner(stream=open(REPORT_FILENAME, "wb"),
                        title="测试报告",
                        tester="bohe",
                        description="Jenkins测试"
                        )
runner.run(suite)
