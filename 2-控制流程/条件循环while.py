"""
=========================================
Author:薄咊
Time:2020-10-18  15:34
comments:python学习
==========================================
"""
"""
while应用：打印100遍hello python:
"""
# 创建一个变量用来保存循环次数
# n = 0
#
# while n < 100:
#     print("hello python")
#     n += 1
#     print("这是第{}遍执行".format(n))
"""
死循环的应用：用户输入用户名或密码错误时提示用户重新输入：
"""
# data = {"user": "python", "password": "python123"}
# while True:
#     # 提示用户输入用户名、密码
#     user = input("请输入用户名：")
#     password = input("请输入密码：")
#
#     if user == data["user"] and password == data["password"]:
#         print("登录成功！")
#         break
#     else:
#         print("您输入的用户名或密码错误！")
"""
while中的break和continue
"""
# 打印到第5遍退出循环：
m = 0
while m < 10:
    m += 1
    print("这是第{}遍打印".format(m))
    if m == 5:
        break
# 第3遍到6遍不打印
n = 0
while n < 10:
    n += 1
    if 3 <= n <= 6:
        continue
    print("这是第{}遍执行".format(n))
