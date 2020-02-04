from S256Point import *
'''
# chapter3

a = FieldElement(0, 223)
b = FieldElement(7, 223)
x1 = FieldElement(192, 223)
y1 = FieldElement(105, 223)
x2 = FieldElement(17, 223)
y2 = FieldElement(56, 223)
p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)
p3 = p1+p2
print(p1+p2)


#3.4
a = FieldElement(0, 223)
b = FieldElement(7, 223)
x = FieldElement(47, 223)
y = FieldElement(71, 223)
p = Point(x, y, a, b)

for s in range(0,220):
    result = s * p
    print(result)
    #print('{}*(47,21)=({},{})'.format(s, result.x.num, result.y.num))

#chapter 3.10
prime = 2**256 - 2**32 - 977
a = FieldElement(0, prime)
b = FieldElement(7, prime)
x = FieldElement(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, prime)
y = FieldElement(0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8, prime)
n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
p = Point(x, y, a, b)
print(n*p)
'''

G = S256Point(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
              0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8)
print(N*G)
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


#2.6
p1 = Point(-1, -1, 5, 7)
print(p1+p1)

a, x1, y1 = 5, -1, -1
s = (3 * x1 **2 + a) / (2 * y1)
x3 = s**2 - 2*x1
y3 = s*(x1-x3)-y1
print(x3, y3)

#ch2.9


# Chapter #1
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