import urllib
import webbrowser
# webbrowser.open('http://www.baidu.com/')
from urllib.error import HTTPError

import requests, chardet
from urllib.request import urlopen


def Web_Data():
    url = 'http://www.people.com.cn/'

    res = requests.get(url)
    try:

        res.encoding = Get_Charset(url)
        print(len(res.text))
        print(res.text[:len(res.text)])
        # 若使用该种写入 则可能会不完整
        # playFile2 = open('webdata2.txt', 'w+')
        # for e in res.text:
        #     playFile2.write(e)
        # 将抓取的文件放在特定文件中
        playFile = open('webdata.txt', 'wb')
        for chunk in res.iter_content(1000000):  # 每次写入100000字节
            playFile.write(chunk)
        playFile.close()
    except:
        print(res.raise_for_status())  # 确保程序下载失败是停止


def Get_Type():
    url = 'http://www.people.com.cn/'
    resp = requests.get(url)
    print(resp.headers['content-type'])
    print(resp.encoding)
    print(resp.apparent_encoding)
    print(requests.utils.get_encodings_from_content(resp.text))


# 获取编码格式
def Get_Charset(url):
    html = urlopen(url).read()
    return chardet.detect(html)['encoding']

#  抓取HTML的相关元素
from urllib.request import urlopen

import chardet
import requests, bs4


def Get_Charset(url):
    html = urlopen(url).read()
    return chardet.detect(html)['encoding']

def isAllChinese(s):
    for c in s:
        if not('\u4e00' <= c <= '\u9fa5'):
            return False
    return True

num=0
def GetDataFromHTML(num):
    url = f"https://movie.douban.com/top250?start={num}& filter="
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
    }

    try:
        res = requests.get(url, headers=headers)
        noStartchSoup = bs4.BeautifulSoup(res.text)
        # 这个时候读取的应该是某个具体的网页
        # exampleFile = open(url)
        # noStartchSoup = bs4.BeautifulSoup(exampleFile.read())
        elems = noStartchSoup.select("span")
        for i in range(len(elems)):
            # print(elems[i])  # 输出的是整个HTML语句
            # print(elems[i].getText())  # 获取语句中的文字
            # print(elems[i].attrs)  # 获取所有的属性及其相关的值
            if elems[i].get('class') is not None:  # 获取属性某个属性的值

                if elems[i].get('class')[0] == 'title':
                    ss = elems[i].getText()
                    if isAllChinese(ss):
                        num +=1
                        new_ss = ss.replace('/', '').lstrip()
                        print(str(num)+":"+new_ss)


    except:
        # print(res.raise_for_status())
        print('error occord')


# 简单控制相关的浏览器
from selenium import webdriver

# 弄成全局变量就不会出现闪退的情况
# chromedriver_path = r'D:\Python\Python37\chromedriver.exe'
# browser = webdriver.Chrome(executable_path=chromedriver_path)

from selenium.webdriver.common.keys import Keys


def Control_Brower():
    url = 'http://www.people.com.cn/index.html'
    # test_brower = browser.get(url)
    # browser.find_element_by_class_name(name)
    # 使用CSS类name的元素
    # browser.find_elements_by_class_name(name)
    # browser.find_element_by_css_selector(selector)
    # 匹配CSS
    # selector的元素
    # browser.find_elements_by_css_selector(selector)
    # browser.find_element_by_id(id)
    # 匹配id属性值的元素
    # browser.find_elements_by_id(id)
    # browser.find_element_by_link_text(text)
    # 完全匹配提供的text
    # 的 < a > 元素
    # browser.find_elements_by_link_text(text)
    # browser.find_element_by_partial_link_text(text)
    # 包含提供的text的 < a > 元素
    # browser.find_elements_by_partial_link_text(text)
    # browser.find_element_by_name(name)
    # 匹配name属性值的元素
    # browser.find_elements_by_name(name)
    # browser.find_element_by_tag_name(name)
    # 匹配标签name的元素
    # browser.find_elements_by_tag_name(name)
    # (大小写无关， < a > 元素匹配'a'和'A')
    # print(brower.find_element_by_class_name('box_nav_all').tag_name)  # .tag_name 表示标签名

    # 获取相关的链接 自动点击链接
    # linkElem = brower.find_element_by_partial_link_text('网友反映特岗教师服务期3个月工资不到账 河南郸城回复：系漏报，责令纠正')
    # linkElem.click()

    # 获取相关的id 进行数据提交
    # emailElem=brower.find_element_by_id('Email')
    # emailElem.send_keys('asdfa')
    # PWDElem.submit() 若是类型是要提交的表格,例如密码

    # Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT 键盘箭头键
    # Keys.ENTER, Keys.RETURN 回车和换行键
    # Keys.HOME, Keys.END,  Home键、End键、
    # Keys.PAGE_DOWN, Keys.PAGE_UP PageUp键和PageDown键
    # Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE Esc、Backspace和字母键
    # Keys.F1, Keys.F2, ..., Keys.F12 键盘顶部的F到Fn2键
    # Keys.TAB Tab键
    # browser.back() 点击“返回”按钮。
    # browser.forward() 点击“前进”按钮。
    # browser.refresh() 点击“刷新”按钮。
    # browser.quit() 点击“关闭窗口”按钮。

    # broswer.refresh()
    # html = browser.find_element_by_tag_name('html')
    # html.send_keys(Keys.END)