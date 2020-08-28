# try/except
# try/except...else
# try-finally
# try：执行代码
# except 发生异常时执行的代码
# else 没有异常时执行的代码
# finally 不管有没异常都会执行的代码

# 抛出异常
def test():
    x = 10
    if x > 5:
        raise Exception('x 不能大于 5。x 的值为: {}'.format(x))


def error_test():
    try:
        test()
    except AssertionError as error:
        print(error)
    else:
        try:
            print("没有异常")
        except AssertionError as error:
            print("还行")
    finally:  # 相当于清理行为
        print("这句话有没有异常都会执行")


# 用户自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
