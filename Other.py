# filter函数用来过滤序列(字符串可以当做序列) 最后返回的是迭代器对象list()可以直接转化

def is_odd(n):
    return n % 2 == 1
# print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))

# 迭代器
def iter_test():
    l = [1, 2, 3, 4]
    it = iter(l)
    for x in it:
        print(x, end=' ')

# 匿名函数
def lambda_f_test():
    sum2 = lambda arg1, arg2: arg1 + arg2
    print("相加后的值为 : %d" % sum2(10, 20))
