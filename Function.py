def function(x):
    a, b = 0, 1
    i = 0
    while i < x:
        print(b, end=' ')  # 在同一末尾添加不同的字符
        a, b = b, a + b
        i = i + 1


# 可变长参数
def function(x, *s):
    print(x)
    print(s)  # s为一个元组


def function(x, **s):
    print(x)
    print(s)  # 此事实参为一个dict
