from FieldElement import *
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