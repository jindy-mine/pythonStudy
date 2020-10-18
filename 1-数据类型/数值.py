"""
=========================================
Author:薄咊
Time:2020-10-12  16:39
comments:python学习:1-数据类型——数值
==========================================
"""
"""
内置函数type():可以用来查看数据类型

1、数值类型：
整数(int)、浮点数（小数，float）、布尔值(bool:True、Flase)

python中的运算符：
    1、算术运算符：+、 -、 *、 /、 //、 %、 **
    # 整数和整数进行除法运算（/）的时候,得到的结果是浮点数
    2、比较预算符：< 、 > 、 <=、  >=、 ==、  !=
    3、赋值运算符：= 、+=、-=、/= 、 *=
    4、逻辑运算符：and（与）、or（或）、not（非）
    5、身份运算符：is 、is not
    6、成员运算符:in not in
"""
import unittest


# class TestStu2(unittest.TestCase):
#     def test_stu2(self):
#         # 数值
#         a = 100
#         b = 2.3
#         c = True
#         # 字符串
#         d = "100"
#         # 元组
#         e = ("100", "name")
#         # 列表
#         f = [1, 2, 3, 4, "name"]
#         # 字典
#         g = {"name": "憨憨", "age": "18"}
#         print(type(a))
#         print(type(b))
#         print(type(c))
#         print(type(d))
#         print(type(e))
#         print(type(f))
#         print(type(g))
"""
python中的随机数：
内置随机数模块：random,需要导入
"""
import random

r1 = random.random()
r2 = random.randint(1, 100)

# print(r1)
# print(r2)
#
# # 随机生成指定范围内的浮点数:随机生成的整数+随机生成的小数
# print(r1 + r2)

s1 = [11,22,33]
s2 = 10
print(id(s1))
print(id(s2))
