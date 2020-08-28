from xml.dom.minidom import parse
import xml.dom.minidom

# getElementsByTagName(xxx) 返回的是一个二维list
def pxml():
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse("movies.xml")
    collection = DOMTree.documentElement  # 根结点
    if collection.hasAttribute("shelf"):  # 判断结点是否有相关属性
        print("Root element : %s" % collection.getAttribute("shelf"))

    # 在集合中获取所有电影
    movies = collection.getElementsByTagName("movie") # 次根结点

    # 打印每部电影的详细信息
    for movie in movies:
        print("*****Movie*****")
        if movie.hasAttribute("title"):
            print("Title: %s" % movie.getAttribute("title"))

        print("Type: %s" % movie.getElementsByTagName('type')[0].childNodes[0].data)
        print("Format: %s" % movie.getElementsByTagName('format')[0].childNodes[0].data)
        print("Rating: %s" % movie.getElementsByTagName('rating')[0].childNodes[0].data)
        print("Description: %s" % movie.getElementsByTagName('description')[0].childNodes[0].data)


def cxml():
    # 在内存中创建一个空的文档
    doc = xml.dom.minidom.Document()
    # 创建一个根节点companys对象
    root = doc.createElement('companys')
    print('添加的xml标签为：', root.tagName)

    # 给根节点添加属性
    root.setAttribute('name', '公司信息')
    # 将根节点添加到文档对象中
    doc.appendChild(root)

    # 给根节点添加一个叶子节点
    company = doc.createElement('gloryroad')
    # 叶子节点下再嵌套叶子节点
    name = doc.createElement('name')
    # 给节点添加文本节点
    name.appendChild(doc.createTextNode('光荣之路'))

    ceo = doc.createElement('CEO')
    ceo.appendChild(doc.createTextNode('吴老师'))
    # 将各叶子节点添加到父节点company中
    company.appendChild(name)
    company.appendChild(ceo)
    # 将company节点添加到根节点companys中
    root.appendChild(company)

    # 此处需要用codecs.open可以指定编码方式
    fp = open(r'company.xml', 'w', encoding='utf-8')
    # 将内存中的xml写入到文件
    doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding='utf-8')
    fp.close()
