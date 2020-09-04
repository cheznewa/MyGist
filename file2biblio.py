import sys
from base58 import b58encode_int
import hashlib
hash = hashlib.sha256()
hash.update(sys.stdin.read())
r = hash.digest()
w = 1+ord(r[0])%6
s = 1+ord(r[1])%8
v = 1+ord(r[2])%32
n = int(sys.argv[1])
a = 0
for m in range(n):
 a = a + ord(r[m+3])*pow(256,m)
print("Address :: " + b58encode_int(a))
print("Wall :: " + str(w))
print("Shelf :: " + str(s))
print("Volume :: " + str(v))