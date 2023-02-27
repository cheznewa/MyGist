# Use The Font :::::: https://github.com/and3rson/graph-bars-font
import sys
from struct import unpack
min = int(sys.argv[1])
max = int(sys.argv[2])
while True:
 o = sys.stdin.read(4)
 n = unpack("I",o)[0]
 if (n >= min) and (n < max):
  i = int((9.0*(n-min)/(float(max)-float(min))))
  sys.stdout.write("%s" %(unichr(12288+i).encode("utf-8")))
