# 模式	描述
# t	文本模式 (默认)。
# x	写模式，新建一个文件，如果该文件已存在则会报错。
# b	二进制模式。
# +	打开一个文件进行更新(可读可写)。
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
# w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
#       如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
#       如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。
#   如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。
#       如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写


# file.flush() 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
# file.fileno() 返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
# file.isatty() 如果文件连接到一个终端设备返回 True，否则返回 False。
# file.read([size]) 从文件读取指定的字节数，如果未给定或为负则读取所有。
# file.readline([size]) 读取整行，包括 "\n" 字符。
# file.readlines([sizeint]) 读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行,
#                           实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。
# file.seek(offset[, whence])移动文件读取指针到指定位置
# file.tell() 返回文件当前位置。
# file.truncate([size]) 从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，
#                       其中 windows 系统下的换行代表2个字符大小。
# file.write(str) 将字符串写入文件，返回的是写入的字符长度。
# file.writelines(sequence) 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。

# 打开一个txt文件 读一行 readline()或read 读多行 readlines() 返回的是一个list每个元素加上\n
def read_txt(name):
    with open(name, "r", encoding='utf-8') as f:
        f_str = f.readlines()
        print(f_str)


# 一行一行的读取文件
def read_txt2(name):
    # 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
    with open(name, "r", encoding='utf-8') as f_str:
        for line in f_str:
            print(line.strip("\n"))  # 去掉换行符


# 写入一个txt 必须写入的是字符串 若不是则需要转换
def write_txt(name):
    with open(name, "a+", encoding='utf-8') as f:
        f.write("\nhello 我是王康")  # 返回的是写入字节的个数


#
import os


# os.getcwd() 获取当前的环境
# os.chdir() 更改当前的环境
#
def test_os():
    os.makedirs("./hello.txt")  # 创建文件夹


# 以二进制的方式保存文件 和 读取文件
import shelve


def test_shelve_write():
    shelveFile = shelve.open("test3")
    cats = ['hello', 'wangkang', 'come on ']
    shelveFile['cats'] = cats
    shelveFile.close()


def test_shelve_open():
    shelveFile = shelve.open("test3")
    print(type(shelveFile))
    print(shelveFile['cats'])
    shelveFile.close()


import pprint


# 漂亮打印
def test_pprint():
    cats = [{'name': 'wangkang', 'age': 25}, {'name': 'xiaowang', 'age': 15}]
    pprint.pformat(cats)
    fileObj = open('mycats.py', 'w')
    fileObj.write('person:' + pprint.pformat(cats) + '\n')
    fileObj.close()
