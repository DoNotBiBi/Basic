# deque
# append(x)， 将x添加到deque的右侧；
#
# appendleft(x)， 将x添加到deque的左侧；
#
# clear()， 将deque中的元素全部删除，最后长度为0；
#
# count(x)， 返回deque中元素等于x的个数；
#
# extend(iterable)， 将可迭代变量iterable中的元素添加至deque的右侧；
#
# extendleft(iterable)， 将变量iterable中的元素添加至deque的左侧，往左侧添加序列的顺序与可迭代变量iterable中的元素相反；
#
# pop()， 移除和返回deque中最右侧的元素，如果没有元素，将会报出IndexError；
#
# popleft()， 移除和返回deque中最左侧的元素，如果没有元素，将会报出IndexError；
#
# remove(value)， 移除第一次出现的value，如果没有找到，报出ValueError；
#
# reverse()， 反转deque中的元素，并返回None；
#
# rotate(n)， 从右侧反转n步，如果n为负数，则从左侧反转，d.rotate(1)
# 等于d.appendleft(d.pop())；
#
# maxlen， 只读的属性，deque的最大长度，如果无解，就返回None；

from collections import deque, Counter


def deque_test():
    queue = deque(['a', 'b', 'c'])
    queue.append('d')
    print(queue)
    queue.popleft()
    print(queue)
    queue.pop()
    print(queue)


def counter_test():
    cnt = Counter()
    wordList = ["a", "b", "c", "c", "a", "a"]
    for word in wordList:
        cnt[word] += 1
    print(cnt)

