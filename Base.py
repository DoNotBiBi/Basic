#!/usr/bin/python3
# int(x [,base])  将x转换为一个整数
# float(x) 将x转换到一个浮点数
#
# complex(real [,imag]) 创建一个复数
#
# str(x) 将对象 x 转换为字符串
#
# repr(x) 将对象 x 转换为表达式字符串
#
# eval(str) 用来计算在字符串中的有效Python表达式,并返回一个对象
#
# tuple(s) 将序列 s 转换为一个元组
#
# list(s) 将序列 s 转换为一个列表
#
# set(s) 转换为可变集合
#
# dict(d) 创建一个字典。d 必须是一个 (key, value)元组序列。
#
# frozenset(s) 转换为不可变集合
#
# chr(x) 将一个整数转换为一个字符
#
# ord(x) 将一个字符转换为它的整数值
#
# hex(x) 将一个整数转换为一个十六进制字符串
#
# oct(x) 将一个整数转换为一个八进制字符串

import keyword
from typing import Set, Any


def print_keywords():
    print(keyword.kwlist)


# 判断x是否是相应的类型
# isinstance() 函数
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型
def judge_int(x) -> bool:
    return isinstance(x, int)


def basic_test():
    # 使用多个变量赋值
    a, b, c = 1, 3, "hello"
    print(a + b)

    tinydict = {'name': 'runoob',
                'code': 1,
                'site': 'www.runoob.com'}
    print(repr(tinydict))  # repr() 是将对象转化为字符串


def basic_test2():
    # 元组的元素是不能修改的
    t = ('abcd', 786, 2.23, 'runoob', 70.2)
    tinytuple = (123, 'runoob')

    print(t)  # 输出完整元组
    print(t[0])  # 输出元组的第一个元素
    print(t[1:3])  # 输出从第二个元素开始到第三个元素
    print(t[2:])  # 输出从第三个元素开始的所有元素
    print(tinytuple * 2)  # 输出两次元组
    print(t + tinytuple)  # 连接元组


def set_test():
    # 集合基本功能是进行成员关系测试和删除重复元素
    # 大括号 { } 或者 set() 函数创建集合
    # 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
    sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
    print(sites)  # 输出集合，重复的元素被自动去掉
    # 成员测试
    if 'Runoob' in sites:
        print('Runoob 在集合中')
    else:
        print('Runoob 不在集合中')

    # set可以进行集合运算
    a: Set[Any] = set('abracadabra')
    b: Set[Any] = set('alacazam')  # set() 里面只有一个参数
    print("a:")
    print(a)
    print("b:")
    print(sorted(b))
    print(a - b)  # a 和 b 的差集
    print(a | b)  # a 和 b 的并集
    print(a & b)  # a 和 b 的交集
    print(a ^ b)  # a 和 b 中不同时存在的元素


def cal_test():
    # / 实际的值
    # // 取整
    # and or not
    # in   not in
    # is   not is
    print(True and False)



