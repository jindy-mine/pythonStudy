"""
=========================================
Author:薄咊
Time:2020-10-16  15:18
comments:python学习:字典
==========================================
"""

dic1 = dict(a=1, b=2, c="hello", d="python")
dic2 = dict([("aa", 1), ("bb", 2), ("cc", "hello"), ("dd", "python")])
# print(dic1)
# print(dic2)
"""
增加键值对：通过键赋值、update
修改值：通过键赋值，有则改，无则加
"""
# 赋值添加：
# dic1["e"] = "你好"
# print(dic1)
# 通过update添加多个键值对，或将两个字典合并到一起
# dic2.update(dic1)
# print(dic2)
"""
删除键值对：pop,popitem
"""
# dic3 = {"a":"hello","b":"python","c":"java"}
# res1 = dic3.pop("a")
# print(dic3)
# print(res1)
# res2=dic3.popitem()
# print(dic3)
# print(res2)
"""查找元素"""
dic4 = {"a":"hello","b":"python","c":"java","d":"php"}
# d1 = dic4["a"]
# print(d1)
# d2 = dic4["e"]
# print(d2)
# d3 = dic4.get("a")
# print(d3)
# d4 = dic4.get("e")
# print(d4)
"""
keys：获取字典中所有的键
values：获取字典中所有的值
items：获取字典中所有的键值对

"""
dic5 = {"a":"hello","b":"python","c":"java","d":"php"}
s1 = dic5.keys()
s2 = dic5.values()
s3 = dic5.items()
print(s1)
print(s2)
print(s3)
#字典的键或值，可以通过list转换成列表查看
print(list(s1))
print(list(s2))
