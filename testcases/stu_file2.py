"""
=========================================
Author:薄咊
Time:2020/9/26  15:42
comments:python学习-1-数据类型：数值、字符串、元组、列表、字典、集合
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


class TestStu2(unittest.TestCase):
    def test_stu2(self):
        # 数值
        a = 100
        b = 2.3
        c = True
        # 字符串
        d = "100"
        # 元组
        e = ("100", "name")
        # 列表
        f = [1, 2, 3, 4, "name"]
        # 字典
        g = {"name": "憨憨", "age": "18"}
        print(type(a))
        print(type(b))
        print(type(c))
        print(type(d))
        print(type(e))
        print(type(f))
        print(type(g))
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

        """
        1.	字符串的定义：
        使用单引号、双引号、三引号包起来；
        单引号和双引号度表示一行字符串，三引号可以用来表示多行字符串；
        空字符串：只有引号，引号中没有任何内容；
        思考：内容中有单引号，如何用字符串表示？ ---使用双引号引起
        # a = “shjaks’sasa”
        2.	字符串的拼接：
        3.	字符串的格式化输出
        4.	字符串转义：
        5.	字符常见的操作方法：
        6.	字符串下标取值和切片操作：
        """
        # str1 = "hello'你好"
        # print(str1)

        # 数值与字符串之间的转换
        # 数值
        # aa = 100
        # bb = 2.3
        # cc = True
        # 整数转换为字符串
        # n1 = str(aa)
        # print(n1, type(n1))
        # # 浮点数转换为字符串
        # n2 = str(bb)
        # print(n2, type(n2))
        # # 布尔值转换为字符串
        # n3 = str(cc)
        # print(n3, type(n3))

        # 3、字符串可不可以转换为数值类型？
        # 01、字符串转换为整数（前提是字符串中都是数字，不能有字母，符号）
        # 02、字符转换浮点数（前提是字符串中都是数字，不能有字母，符号）
        # 03、字符串转换为布尔值（都可以转）
        # 空字符串的bool值为False,其他的都是为True
        # print(int("789"))
        # print(float("67.89"))
        # print(bool(""))
        # print(bool("?"))

        # 2、整数、浮点数、布尔值直接可不可以进行相互转换（可以的）

        # 浮点数转换为整数
        # print(int(1.1))
        # # 布尔值转换为整数：True的整数值为1，False的整数值为0
        # print(int(False))
        #
        # # 整数和布尔值转换为浮点数
        # print(float(11))
        # print(float(True))
        #
        # # 整数和浮点数转换为布尔值：（只要不是0,布尔值都为True）
        # print(bool(11))
        # print(bool(-1.011))
        # print(bool(0))

        # python中的任何数据都可以转换为布尔值
        # 数值中0的值为False
        # 字符串中空字符为Flase
        """
        字符串的拼接：
        第一种方法：使用 + 对字符串进行拼接
        
        第二种方法：使用字符串的join方法进行拼接
        """
        s1 = "你好"
        s2 = "python"
        s3 = s1 + "," + s2
        s4 = "_".join((s1, s2))
        s5 = "".join((s1, s2))
        s6 = "-".join(s2)
        print(s3)
        print(s4)
        print(s5)
        print(s6)

        s3 = "姓名%s,考试成绩%s" % ("张三", 98.5)
        s4 = "姓名%s,考试成绩%d" % ("张三", 98.5)
        s5 = "姓名%s,考试成绩%f" % ("张三", 98.5)
        # 限制小数的显示位数:
        s6 = "姓名%s,考试成绩平均分%.2f" % ("张三", 98.333333333)
        print(s3)
        print(s4)
        print(s5)
        print(s6)

        # F表达式(扩展)
        # name = input("输入名字:")
        # info = input("输入费用信息：")
        # money = input("输入金额：")
        # s1 = F"今天收到{name}，交来{info},{money}.开此收据为凭证"
        # print(s1)

        """
        format的使用
        
        注意点：input输入的，不管你输的是什么，都会保存为字符串
        """

        # name = input("输入名字:")
        # info = input("输入费用信息：")
        # money = float(input("输入金额："))
        # # 通过索引来控制填充的位置
        # print("今天收到{2}，交来{0}{1}.开此收据为凭证".format(info, money, name))

        # 保留指定小数位数
        # print("今天收到{}，交来{},￥:{:.3f}开此收据为凭证".format("憨憨", "学费", 999.222222223332))

        # 指定占位的字符串长度
        # 默认左对齐
        # print("python:{:10}AAAAAAAAAAAAAAAA".format("123"))
        # # 左对齐
        # print("python:{:<10}AAAAAAAAAAAAAAAA".format("123"))
        # # 右对齐
        # print("python:{:>10}AAAAAAAAAAAAAAAA".format("123"))
        # # 居中对齐
        # print("python:{:^10}AAAAAAAAAAAAAAAA".format("123"))
        #
        # # 指定内容填充
        # print("python:{:q<10}AAAAAAAAAAAAAAAA".format("123"))
        #
        # # 百分比显示效果
        # print("百分比为：{:.3%}".format(0.2))

        """
        字符串的转义：
        \表示转义
        \t:制表符
        \n:换行符
        \\:表示\
        # 如何关闭字符串转义
        字符串：r表达式
        
        
        """
        # s1 = "python\thello"
        # s2 = "python\nppppp"
        # # 使用字符串r表达式关闭转义
        # s3 = r"python\thello"
        # s4 = r"python\nppppp"
        # print(s1)
        # print(s2)
        # print(s3)
        # print(s4)
