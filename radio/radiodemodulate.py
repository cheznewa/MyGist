import sys
from struct import pack
m=0
oo=0
while True:
 o = sys.stdin.read(2)
 o = ord(o[0])+(ord(o[1])*256)
 if o < oo:
  a = float(sys.argv[1])*m
  sys.stdout.write(pack("I",int(a)))
  oo=0
  o=0
  n=0
  m=0
 n=abs(o-oo)
 m = (m+n)/2
 oo=o