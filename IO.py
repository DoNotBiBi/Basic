# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式
import math


def repr_test():
    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')  # 注意前一行 'end' 的使用
        print(repr(x * x * x).rjust(4))


def zfill_test():
    print('12'.zfill(7))


def strformat_test():
    print('年龄为{age},生日为{birth}'.format(age=2, birth=1218))
    print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))  # 小数点后保留三位小数
    print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'baidu', other='Taobao'))
    table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
    print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))  #可以保证其类型以及精确度