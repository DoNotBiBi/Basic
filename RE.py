#  todo:
#      学习第七章
import re


# 简单的正则表达式--寻找电话号码
def test_base_re():
    # 1、创建一个Regex对象
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    # 2、使用search()方法传入想查找的字符串。返回一个Match对象
    mo = phoneNumRegex.search('my number is 123-456-4561')
    # 3、调用group()方法，返回实际匹配文本的字符串
    print('Phone number found :' + mo.group())


def test_base_re2():
    # 1、创建一个Regex对象 需要注意的是：若是匹配的是符号 需要转义符号\
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    # 2、使用search()方法传入想查找的字符串。返回一个Match对象
    # serach() 匹配只有一个字符串 即使匹配多个字符串也只返回一个Match对象
    mo = phoneNumRegex.search('my number is 123-456-4561')
    # 3、调用group()方法，返回实际匹配文本的字符串
    print('Phone number found :' + mo.group())
    # 调用groups()方法 返回的是多个值的元组 `
    for nums in mo.groups():
        print(nums)


# | 匹配多个分组
# (xx)? 表示xx是可有可无
# (xx)* 表示xx匹配0次或多次
# (xx)+ 表示xx至少匹配一次
# (xx){m,n} 表示xx匹配m~n次 m若是省略默认为0，n若是省略默认为大于m次
#           返回的是贪心匹配 即最长字符串
# (xx){m,n}?  返回的是非贪心匹配，即最短字符串
# \d 0-9的数字
# \D 除开0-9的任何字符
# \w 任何字母、数字、下划线字符
# \W 除开字母、数字、下划线字符的任何字符
# \s 空格、制表符、换行符
# \S 除开空格、制表符、换行符的任何字符
def test_base_re3():
    phoneNumRegex = re.compile(r'num(ber|bers|N|)')
    # findall() 返回的是所以匹配的字符串，返回的是一个list
    mo = phoneNumRegex.findall('number is one of numbers,and numN')
    print(mo)
    for nums in mo:
        print(nums)


# ^ 表示 非
# $ 表示结束 eg:\d$表示以数字结尾的字符串 ^\d+$ 从头到尾都是数字的字符串
# (.*) 通配符 匹配任意文本 但不包括换行符号
# compile()的第二个参数 可以混合来用，用| 隔开
# re.DOTALL 匹配任意文本，包括换行符号
# re.I re.IGNORECASE 忽略大小写
# re.VERBOSE
def test_base_re4():
    phoneNumRegex = re.compile(r'[uon]')
    mo = phoneNumRegex.findall('number is one of numbers,and numN')
    print(mo)

    phoneNumRegex2 = re.compile(r'[^uon]')
    mo2 = phoneNumRegex2.findall('number is one of numbers,and numN')
    print(mo2)

    phoneNumRegex3 = re.compile(r'\d$')
    mo3 = phoneNumRegex2.search('number is one of numbers,and numN6')
    print(mo3 == None)

    # 若不加 ？ 则贪心匹配
    r = re.compile(r'<.*?>')  # 非贪心匹配
    mo = r.search('<hello wangkang> for world>')
    print(mo.group())


def test_base_sub():
    nameRegex = re.compile(r'Agent (\w)\w*', re.I)
    newname = nameRegex.sub('\1******', 'Agent alice gave the secret document to agent bob')
    print(newname)

# todo
#  从粘贴复制中提取电话号码和邮箱,有点小问题
import pyperclip
def test():
    phoneRegex = re.compile(r'''
        (\d{3}|(\d{3}\))?
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)
        (\d{4})
        (\s*(ext|x|ext.)\s*(\d{2,5}))?
        )''', re.VERBOSE)

    emailRegex = re.compile(R'''
        [a-zA-Z0-9.%+-]+
        @
        [a-zA-Z0-9.-]+
        (\.[a-zA-Z]{2,4})
        ''', re.VERBOSE)

    text=str(pyperclip.paste())
    matchs=[]
    for groups in phoneRegex.findall(text):
        phoneNum='-'.join([groups[1],groups[3],groups[5]])
        if groups[8] !='':
            phoneNum += ' x'+groups[8]
    for groups in emailRegex.findall(text):
        matchs.append(groups[0])

    if len(matchs)>0:
        pyperclip.copy('\n'.join(matchs))
        print('copied to clipbord')
        print('\n'.join(matchs))
    else:
        print("nothing to find")
