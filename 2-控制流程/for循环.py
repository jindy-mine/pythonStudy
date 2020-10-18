"""
=========================================
Author:薄咊
Time:2020-10-18  16:45
comments:python学习
==========================================
"""
"""
语法结构：
for 变量 in XXX:
    #每次循环遍历出来数据后执行的代码
"""
# stu = ["桃子", "西瓜", "樱桃", "苹果", "香蕉"]
# for i in stu:
#     print(i)

"""
遍历成绩后，区分等级
"""
# li = [66, 47, 83, 57, 99]
# for item in li:
#     print("本次遍历出来的成绩为：{}".format(item))
#     if item < 60:
#         print("成绩不及格！")
#     elif 60 <= item <= 80:
#         print("成绩及格！")
#     elif 80 <= item <= 100:
#         print("成绩优秀！")

"""
两种方法实现1+2+3+...+100
"""
# while循环：
# n = 1
# # s：相加结果
# s = 0
# while n <= 100:
#     s += n
#     n += 1
# print(s)
#
# # for循环：
# ss = 0
# for i in range(1, 101):
#     ss += i
# print(ss)


"""
遍历字典：键、值、键值对
"""
# dic = {"a": 11, "b": 22, "c": 33}
# 遍历字典的键：
# for i in dic:
#     print(i)
#
# for j in dic.values():
#     print(j)
# for k in dic.items():
#     print(k)
"""
扩展：元组拆包（列表、字符串）,元组内有几个值，就需要定义几个变量接收
"""
# tu = (11, 22)
# a, b = tu
# print(a)
# print(b)

# 定义两个变量接收字典的键和值
# for k,v in dic.items():
#     print(k)
#     print(v)

"""
for循环中的跳出循环：
break:
continue:
"""
# 打印5遍hello python
# for i in range(1, 6):
#     print(i)

# 打印第4遍跳出循环
# for i in range(1, 6):
#     print(i)
#     if i == 4:
#         break

# 第2-4遍不打印
# for i in range(1, 6):
#     if 2 <= i <= 4:
#         continue
#     print(i)
"""
for--else语法：
只有当循环是通过break结束的时候不会执行，其他情况都会执行
"""
# for i in range(5):
#     print("本轮遍历的数据为{}".format(i))
#     if i == 3:
#         break
# else:
#     print("for对应的else")
"""
# # 判断用户是否存在
"""
# users = ["bohe", "apple", "orange", "pick"]

# user = input("请输入您的账号：")
# for item in users:
#     if user==item:
#         print("该用户已存在！")
#         break
# else:
#     print("用户不存在！")
"""
打印三角形
"""
"""直角三角形"""
# for i in range(5):
#     for j in range(i+1):
#         print("* ",end="")
#     print()
"""正等腰三角形"""
# n = int(input("请输入行数："))
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(n-i,n):
#             print("* ",end="")
#     print()
"""倒等腰三角形"""
for i in range(5):
    for j in range(i):
        print(" ", end="")
    for k in range(i, 5):
        print("* ", end="")
    print()
