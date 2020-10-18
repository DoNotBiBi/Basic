# 异常只要没有被处理，python就会反向跟踪
import traceback # 反向追踪错误信息
def boxPrint(sympol,width,height):
    if len(sympol) !=1:
        raise Exception('Symole must be a single character string') # 抛出异常
    if width <=2:
        raise Exception('width must be greater than 2')
    if height <=2:
        raise Exception('height must be greater than 2')
    print(sympol*width)
    for i in range (height*2):
        print(sympol+(' '*(width-2))+sympol)
    print(sympol*width) # 多次打印
# for sym,w,h in(('*',4,4),('0',20,5),('x',1,3),('zz',3,3)):
#     try:
#         boxPrint(sym,w,h)
#     except Exception as err:
#         print('An exception happened:'+str(err))
def test_traceback():
     try:
         raise Exception('This is the error message')
     except:
         errorFile=open('errorInfo.txt','w')
         errorFile.write(traceback.format_exc())  # tracebask_format_exc() 返回错误的字符串形式
         errorFile.close()
         print('The traceback info was written to errorInfo.txt')
# 断言 确保代码明显的错误 但是缺陷就是减慢程序的速度
# assert <返回bool的条件>, <条件为false时显示的字符串>
# 通过Python -O 可以禁用 断言
def test_assert():
    t='hello'
    assert t=='open', 't open need to be open'


# 使用日志 logging 
# 禁用日志 logging.disable() 参数为下面的对应的函数
# 日志级别 对应函数
# DEBUG logging.debug()
# INFO logging.info()
# WARNING logging.warning()
# ERROR  logging.error()
# CRITICAL logging.critical()
# 若是先将日志的相关信息放在文件，在只需在对应的函数的第一个函数为filename='xxx'
import logging
logging.basicConfig(level=logging.DEBUG,format= '%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of program')
def factorial(n):
    logging.debug(f'start of factorial({n})')
    total=1
    for i in range(1,n+1):
        total *= i
        logging.debug(f'i is {i} + total is {total}')
    logging.debug(f'end of factorial({n}')
    return total
print(factorial(6))
logging.debug('endo of program')