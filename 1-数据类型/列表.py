"""
=========================================
Author:薄咊
Time:2020-10-13  14:33
comments:python学习：1-数据类型——列表
==========================================
"""
"""
列表的增加元素:append、insert、extend
"""
li = ["hello", ["red"], 111]
# li.append((222, 333))
# print(li)
# li.insert(1, "python")
# print(li)
# li.extend(["php", "java"])
# print(li)

"""
列表的删除元素:remove、pop、clear
"""
li1 = ["hello", "你好", "python", "world", "php", "你好", "python", "php", "world", "你好", "php", "python", "world"]

# li1.remove("php")
# print(li1)
# li1.pop()
# print(li1)
# li1.pop(3)
# print(li1)
# li1.clear()
# print(li1)

# li2 = ["hello","你好","python","world","php"]
# li2[1]="hi"
# print(li2)

# li3 = ["hello", "你好", "python", "world", "php", "你好", "python", "php", "world", "你好", "php", "python", "world"]
# res = li3.index("python")
# print(res)
# res1 = li3.index("python", 3)
# print(res1)
# res2 = li3.index("python", -8, -1)
# print(res2)
# res3 = li3.count("python")
# print(res3)
"""
列表中其他方法：sort、reverse、copy
"""

# li4 = [6, 5, 7, 8, 3, 4, 5, 7, 8, 66, 1, 2, 4, 55, 322, 445]
# # 反向输出
# li4.reverse()
# print(li4)
# # 排序，默认升序
# li4.sort()
# print(li4)
# # 降序排序
# li4.sort(reverse=True)
# print(li4)
# li5 = li4.copy()
# print(li5)
# print(id(li5))
# print(id(li4))

"""
内置函数len:可以查看字符串、列表、元组、字典、集合的元素总数
"""
aaa = "sdashsakdhakshdkas"
res = len(aaa)
print(res)