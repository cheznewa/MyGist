import sys
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-+"
import hashlib
hash = hashlib.sha256()
hash.update(sys.stdin.read())
r = hash.digest()
w = 1+ord(r[0])%6
s = 1+ord(r[1])%8
v = 1+ord(r[2])%64
n = int(sys.argv[1])
a = 0
for m in range(n):
 a = a + ord(r[m+3])*pow(256,m)
t = ""
while a:
 a,q = divmod(a,28)
 t = alpha[q] + t
sys.stdout.write("Address :: %s\n" %(t))
sys.stdout.write("Wall :: %s\n" %(w))
sys.stdout.write("Shelf :: %s\n" %(s))
sys.stdout.write("Volume :: %s\n" %(v))