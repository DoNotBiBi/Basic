# python->Json
# dict	object
# list, tuple	array
# str	string
# int, float, int- & float-derived Enums	number
# True	true
# False	false
# None	null

# Json -> python

import json


def pjson_test():
    # Python 字典类型转换为 JSON 对象
    data1 = {
        'no': 1,
        'name': 'Runoob',
        'url': 'http://www.runoob.com'
    }

    json_str = json.dumps(data1)
    print("Python 原始数据：", repr(data1))
    print("JSON 对象：", json_str)

    # 将 JSON 对象转换为 Python 字典
    data2 = json.loads(json_str)
    print("data2['name']: ", data2['name'])
    print("data2['url']: ", data2['url'])


# 读取json文件
def pjson_read():
    with open('data.json', 'r') as f:
        data = json.load(f)
    print(data)


def pjson_write():
    data = {
        'name': 'tianzhongli',
        'age': 1,
        'gender': 'male'
    }
    with open('data2.json', 'w') as f:
        json.dump(data, f)
