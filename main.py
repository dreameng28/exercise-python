#coding=utf-8
from dominate.tags import a

__author__ = 'dreameng'

import time
import os

cont = ["a", 'c', 'dd', 'eee', 'a', 'a', 'eee']
print(cont)

a = u'哈哈哈'
print len(a)
print len(u'呵呵')

a = (u'很好', u'hehe', u'haha')
print a

a = '''foahfahh
japfhoawhf
foahvfoah'''

print a

a = [u'你好', u'hfoahf', u'aohfo']
a[1] = 0
a.append(11)
print a[-4]

a = (9,['hh', (11, 3, 3)])
a[1].append(999)
print a
if 10:
    print 11 > 12

b = 1
b += 1
print b

s = 0
for i in range(101):
    s += i
print s



print '-----------------------'
l = {}
t = time.time()
for i in range(100000):
    l[str(i)] = i
print time.time() - t
print '-----------------------'

t2 = time.time()
a = l.get('1000')
print time.time() - t2



print '-----------------------'
l = []
t = time.time()
for i in range(100000):
    l.insert(0, i)
print time.time() - t
print '-----------------------'

t2 = time.time()
a = l.index(1)
print time.time() - t2

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print fact(10)

a = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff']
b = a[:-1]
print b

d = u'哈哈哈'
e = d[::2]
print e

d = {'a': 1, 'b': 2, 'c': 3}
for key, value in d.iteritems():
    print key + ": " + str(value)

for i, j in enumerate(['a', 'b', 'c']):
    print i, j

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y

a = [x*x for x in range(1, 10) if x % 2 == 0]
print a

a = [m + n for m in 'ABC' for n in 'XYZ']
print a

a = [d for d in os.listdir('/Users/dreameng/Downloads')]
for x in a:
    print x

s = 'AdC111'
s2 = s.upper()
print s2

def f(arg):
    return arg*arg
a = map(f, [1, .3, 2])
print a

# 创建g2和g1的区别仅在于最外层的[]和()，g2是一个list，而g1是一个generator。
g1 = (x * x for x in range(10))
g2 = [x * x for x in range(10)]

g1.next()
print g1.next()
g1.close()
for x in g1:
    print x

def fib(max1):
    n1, a1, b1 = 0, 0, 1
    while n1 < max1:
        yield b1
        a1, b1 = b1, a1 + b1
        n1 += 1


for x in fib(6):
    print x

def ff():
    yield 1
    print '111'
    yield 2
    print '222'
    yield 3
    print '333'


v = fib(6)
print v.next()
print v.next()
print v.next()
print v.next()

