from S256Point import *
from Signature import *
from PrivateKey import *
from io import BytesIO
from Script import *
from Tx import *


#5.5
hex_transaction = '010000000456919960ac691763688d3d3bcea9ad6ecaf875df5339e148a1fc61c6ed7a069e010000006a47304402204585bcdef85e6b1c6af5c2669d4830ff86e42dd205c0e089bc2a821657e951c002201024a10366077f87d6bce1f7100ad8cfa8a064b39d4e8fe4ea13a7b71aa8180f012102f0da57e85eec2934a82a585ea337ce2f4998b50ae699dd79f5880e253dafafb7feffffffeb8f51f4038dc17e6313cf831d4f02281c2a468bde0fafd37f1bf882729e7fd3000000006a47304402207899531a52d59a6de200179928ca900254a36b8dff8bb75f5f5d71b1cdc26125022008b422690b8461cb52c3cc30330b23d574351872b7c361e9aae3649071c1a7160121035d5c93d9ac96881f19ba1f686f15f009ded7c62efe85a872e6a19b43c15a2937feffffff567bf40595119d1bb8a3037c356efd56170b64cbcc160fb028fa10704b45d775000000006a47304402204c7c7818424c7f7911da6cddc59655a70af1cb5eaf17c69dadbfc74ffa0b662f02207599e08bc8023693ad4e9527dc42c34210f7a7d1d1ddfc8492b654a11e7620a0012102158b46fbdff65d0172b7989aec8850aa0dae49abfb84c81ae6e5b251a58ace5cfeffffffd63a5e6c16e620f86f375925b21cabaf736c779f88fd04dcad51d26690f7f345010000006a47304402200633ea0d3314bea0d95b3cd8dadb2ef79ea8331ffe1e61f762c0f6daea0fabde022029f23b3e9c30f080446150b23852028751635dcee2be669c2a1686a4b5edf304012103ffd6f4a67e94aba353a00882e563ff2722eb4cff0ad6006e86ee20dfe7520d55feffffff0251430f00000000001976a914ab0c0b2e98b1ab6dbf67d4750b0a56244948a87988ac005a6202000000001976a9143c82d7df364eb6c75be8c80df2b3eda8db57397088ac46430600'
stream = BytesIO(bytes.fromhex(hex_transaction))
tx_obj = Tx.parse(stream)
print(tx_obj.tx_ins[1].script_sig)
print(tx_obj.tx_outs[0].script_pubkey)
print(tx_obj.tx_outs[1].amount)
print(tx_obj.fee())

hex_transaction = '0100000001c228021e1fee6f158cc506edea6bad7ffa421dd14fb7fd7e01c50cc9693e8dbe02000000fdfe0000483045022100c679944ff8f20373685e1122b581f64752c1d22c67f6f3ae26333aa9c3f43d730220793233401f87f640f9c39207349ffef42d0e27046755263c0a69c436ab07febc01483045022100eadc1c6e72f241c3e076a7109b8053db53987f3fcc99e3f88fc4e52dbfd5f3a202201f02cbff194c41e6f8da762e024a7ab85c1b1616b74720f13283043e9e99dab8014c69522102b0c7be446b92624112f3c7d4ffc214921c74c1cb891bf945c49fbe5981ee026b21039021c9391e328e0cb3b61ba05dcc5e122ab234e55d1502e59b10d8f588aea4632102f3bd8f64363066f35968bd82ed9c6e8afecbd6136311bb51e91204f614144e9b53aeffffffff05a08601000000000017a914081fbb6ec9d83104367eb1a6a59e2a92417d79298700350c00000000001976a914677345c7376dfda2c52ad9b6a153b643b6409a3788acc7f341160000000017a914234c15756b9599314c9299340eaabab7f1810d8287c02709000000000017a91469be3ca6195efcab5194e1530164ec47637d44308740420f00000000001976a91487fadba66b9e48c0c8082f33107fdb01970eb80388ac00000000'
stream = BytesIO(bytes.fromhex(hex_transaction))
tx_obj = Tx.parse(stream)
print(tx_obj.tx_ins[0].script_sig)
print(tx_obj.tx_outs[0].script_pubkey)
print(tx_obj.tx_outs[1].amount)
print(tx_obj.fee())

'''
# chapter4

#4.1
priv = PrivateKey(5000)
print(priv.point.sec(compressed=False).hex())

#4.2
priv = PrivateKey(5001)
print(priv.point.sec(compressed=True).hex())

#4.3
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec

sig = Signature(r, s)
print(sig.der().hex())

#4.5
priv = PrivateKey(5002)
print(priv.point.address(compressed=False, testnet=True))

#4.6
priv = PrivateKey(5003)
print(priv.wif(compressed=False, testnet=True))

#4.9
priv = PrivateKey(50)
print(priv.point.address(compressed=False, testnet=True))

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


z = 0xbc62d4b80d9e36da29c16c5d4d9f11731f36052c72401a76c23c0fb5a9b74423
r = 0x37206a0610995c58074999cb9767b87af4c4978db68c06e8e6e81d282047a7c6
s = 0x8ca63759c1157ebeaec0d03cecca119fc9a75bf8e6d0fa65c841c8e2738cdaec
px = 0x04519fac3d910ca7e7138f7013706f619fa8f033e6ec6e09370ea38cee6a7574
py = 0x82b51eab8c27c66e26c858a079bcdf4f1ada34cec420cafc7eac1a42216fb6c4
point = S256Point(px, py)
s_inv = pow(s, N-2, N)
u = z * s_inv % N
v = r * s_inv % N
print((u*G + v*point).x.num == r)

#3.12.6
from helper import hash256


e = int.from_bytes(hash256(b'my secret'), 'big')
z = int.from_bytes(hash256(b'my message'), 'big')
k = 1234567890
r = (k*G).x.num
k_inv = pow(k, N-2, N)
s = (z+r*e) * k_inv % N
point = e*G
print(point)
print(hex(z))
print(hex(r))

aa = PrivateKey(12345)
zz = int.from_bytes(hash256(b'Programming Bitcoin!'), 'big')
print(zz)


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