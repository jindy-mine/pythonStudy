"""
=========================================
Author:薄咊
Time:2020/9/28  0:14
comments:python学习
==========================================
"""


class TestStu4():

    def get_datas(self):
        a = [1, 2, 3, 4, 6, 3, 2, 4, 5, 7, 8, 9, 6, 3, 5, 6, 4, 3, 23, 5, 6, 7, 4, 2, 2, 0, 9, 8, 7, 6, 4, 7, 6, 5, 3,
             8, 4]
        result = []
        data_dict = {}
        for item in set(a):
            data_dict[str(item)] = a.count(item)
        print(data_dict)
        res = sorted(data_dict.values(),reverse=True)
        for num in res:
            for key,value in data_dict.items():
                if num == value and key not in result:
                    result.append(key)
        return result

if __name__ == '__main__':
    result = TestStu4().get_datas()
    print(result)