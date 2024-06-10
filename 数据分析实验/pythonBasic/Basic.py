# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年12月28日
"""

'''基本操作'''
print('hello world ' * 3)

string1 = 'hello world'
print(string1[1:3])  # 字符串的切片操作，切片时左闭右开
print(string1[2:])
print(string1[-1:])  # 打印d，并非全部

# fruit=[] () {key:value}   列表 元祖 字典
fruit1 = []
type(fruit1)  # 查看新变量的数据类型

'''列表'''
list1 = [0.25, 'hello', True, [2.3, 1.5]]
list2 = list('ABCD')  # ['A', 'B', 'C', 'D']
list3 = [1, 2] + [3, 4]  # 将两个列表中的元素进行合并

# 删除列表中的元素
list1.remove('hello')  # 删除列表中的指定元素
del list1[0:2]  # 删除列表中的多个元素
del list1  # 删除列表本身

# 修改列表中的元素
all_in_list = [0.25, 'hello', True, [2.3, 1.5]]
all_in_list[0] = 125  # 通过赋值来修改列表中的元素

'''字典'''
dict_1 = {
    'the': 2,
    3.4: [2.5, 3],
    'hello': 'world'
}

dict_1['the'] = 101  # 修改字典中的值
dict_1['language'] = 'python'  # 通过赋值来新增键值对
dict_1.update({'hello world': 3, 4.5: [2.3, 1.2]})
del dict_1['the']  # 删除字典中的指定的键值对

dict_1.keys()  # 访问字典的所有键
dict_1.values()  # 访问字典的所有值
dict_1.items()  # 访问字典的所有元素

dict_2 = {i: i ** 2 for i in range(1, 11)}  # 字典推导式

'''多路分支语句'''
if 1 > 2:
    pass
elif 2 < 3:
    print('world')
else:
    print('hello')

# continue跳过本次循环，break跳出循环

yes = 1
if (True):
    try:
        print(yes)
    except:
        print('no')  # 当yes未被定义时打印no字符串，但是这里我在pycharm的控制台里运行会直接输出yes

    '''函数'''
    #  使用lambda创建匿名函数
    y = lambda x: x ** 2
    y(10)
    y(x=5)

    #  导入模块中的目标函数
    #  from def_mdule import def_mean, y, pi

    '''创建类'''


    class Human:
        '''在 Python 中，如果不显式定义构造函数 __init__，系统会自动为你创建一个默认的构造函数。
        这个默认构造函数不做任何事情，它只是简单地将对象创建出来而已。因此，如果你没有定义构造函数，
        Python 会使用这个默认的构造函数来初始化对象。'''

        def __init__(self, age, gender):  # 构造函数
            self.age = age  # 类的属性
            self.gender = gender

        def sqrt(self, x):
            return x ** 2

zhangfei = Human(age=23, gender='男')
zhangfei.age  # 对象的属性
zhangfei.gender
zhangfei.sqrt(10)  # 调用对象的方法
