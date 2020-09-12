#!/usr/bin/python3
# 类的专用方法
# __init__ : 构造函数，在生成对象时调用
# __del__ : 析构函数，释放对象时使用
# __repr__ : 打印，转换
# __setitem__ : 按照索引赋值
# __getitem__: 按照索引获取值
# __len__: 获得长度
# __cmp__: 比较运算
# __call__: 函数调用
# __add__: 加运算
# __sub__: 减运算
# __mul__: 乘运算
# __truediv__: 除运算
# __mod__: 求余运算
# __pow__: 乘方
# 运算符重载
# def __add__(self, other):
#     return Vector(self.a + other.a, self.b + other.b)
# def __str__(self):
#     return 'Vector (a, b)' .format (a=self.a, b=self.b)
#  类的基本定义
class Base_class:
    def __init__(self, name, animal):  # 类的实例化操作会自动调用 __init__() 方法
        """

        :type animal: object
        """
        self.name = name
        self.animal = animal

    def print_name(self):
        print(f"this animal is {self.name}")


# 继承
class Dog(Base_class):  # 多个继承，用逗号分隔开
    def __init__(self, name, animal, colour, age):
        super().__init__(name, animal)  # 保证父类被初始化
        self.colour = colour
        self.__age = age  # 私有属性

    def __print_age(self):  # 私有方法
        print(f"this animal age is {self.__age}")

    # 重写方法
    def print_name(self):
        self.__print_age()  # 私有方法只能在类中使用
        super().print_name()  # 调用父类的方法
        print(f"this animal is {self.name},and colour is {self.colour}")
