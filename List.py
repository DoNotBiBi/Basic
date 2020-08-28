# 1	list.append(obj)
# 在列表末尾添加新的对象
# 2	list.count(obj)
# 统计某个元素在列表中出现的次数
# 3	list.extend(seq)
# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4	list.index(obj)
# 从列表中找出某个值第一个匹配项的索引位置
# 5	list.insert(index, obj)
# 将对象插入列表
# 6	list.pop([index=-1])
# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7	list.remove(obj)
# 移除列表中某个值的第一个匹配项
# 8	list.reverse()
# 反向列表中元素
# 9	list.sort( key=None, reverse=False)
# 对原列表进行排序
# 10	list.clear()
# 清空列表
# 11	list.copy()
# 复制列表
def list_test():
    l = ['abcd', 786, 2.23, 'ru', 70.2]
    tinylist = [123, 'ru']

    print(l)  # 输出完整列表
    print(l[0])  # 输出列表第一个元素
    print(l[1:3])  # 从第二个开始输出到第三个元素 默认第三个元素为0
    print(l[2:])  # 输出从第三个元素开始的所有元素
    print(tinylist * 2)  # 输出两次列表
    print(l + tinylist)  # 连接列表
    print(l[::-1])  # 逆序输出
    # 删除列表元素
    del l[2]
    print('这是删除过后的list：')
    print(l)

    # 列表的单个元素或多个可以更改
    a = [1, 2, 3, 4, 5, 6]
    print(a)
    a[0] = 9
    print(a)
    a[2:5] = [13, 14, 15]
    print(a)
    a[2:5] = []
    print(a)

    print('a的长度是 %d' % len(a))
    print('a的最大值为%d' % max(a))
    print('a的最小值为%d' % min(a))
    a = (1, 2, 3)
    print(list(a))  # 将元组转换为列表

    l2 = [2, 5, 1, 7, 3, 9]
    l2.sort(key=None, reverse=True)  # reverse=False是升序（默认状态） True是逆序
    print(l2)
    