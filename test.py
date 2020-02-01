from FieldElement import *
from Point import *

'''
#p1 = Point(2, 4, 5, 7)
p2 = Point(-1, -1, 5, 7)
p3 = Point(18, 77, 5, 7)
#p4 = Point(5, 7, 5, 7)

print(p2!=p3)

p1 = Point(-1, -1, 5, 7)
p2 = Point(-1, 1, 5, 7)
inf = Point(None, None, 5, 7)

print(1)
print(p1 + inf)
print(2)
print(inf + p2)
print(3)
print(p1 + p2)

#2.4
p1 = Point(2, 5, 5, 7)
p2 = Point(-1, -1, 5, 7)
print(p1)
print(p2)
p3 = p1+p2
print(p3)
'''

#2.6
p1 = Point(-1, -1, 5, 7)
print(p1+p1)

a, x1, y1 = 5, -1, -1
s = (3 * x1 **2 + a) / (2 * y1)
x3 = s**2 - 2*x1
y3 = s*(x1-x3)-y1
print(x3, y3)

#ch2.9


'''
Chapter #1
a = FieldElement(3, 13)
b = FieldElement(12, 13)
c = FieldElement(10, 13)
print(a)
print(b)
print(c)
print(a==b)
print(a==a)
print(a!=b)
print(a!=a)
print(a+a)
print(a+b)
print(a+c)
print(b+c)
print(a+b==c)

print(a-a)
print(a-b)
print(b-a)
print(a-c)
print(c-a)
print(b-c)
print(c-b)
print(a-b==c)

#p49 ex1.5
prime = 19
for k in (1,3,5,7,13,18):
    print([k*i % prime for i in range(0, prime)])

for k in (1,3,5,7,13,18):
    print(sorted([k*i % prime for i in range(0, prime)]))

print(a*b==c)

#p49 ex1.7
for k in (7, 11, 17, 31):
    print([pow(i, k-1, k) for i in range(1, k)])
'''