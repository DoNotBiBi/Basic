# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式
import math


def repr_test():
    for x in range(1, 11):
        print(repr(x).rjust(1), repr(x * x).rjust(3), end=' ')  # 注意前一行 'end' 的使用
        print(repr(x * x * x).rjust(4))


def zfill_test():
    print('12'.zfill(7))


def f_string_test():
    print(f'年龄为{2},生日为{1218}')
    print(f'常量 PI 的值近似为 {math.pi:.3f}。')  # 小数点后保留三位小数
    print(f'站点列表 {"Google"}, {"baidu"}, 和 {"Taobao"}。')
    table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
    print(f'Runoob: {table["Runoob"]:d}; Google: {table["Google"]:d}; Taobao: {table["Taobao"]:d}')  #可以保证其类型以及精确度
