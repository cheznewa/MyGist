import sys
from struct import unpack
while True:
 o = sys.stdin.read(4)
 n = unpack("I",o)[0]
 m=0
 while m < 65536:
  sys.stdout.write("%s%s" %(chr(int(m%256)),chr(int(m/256))))
  m=m+(n/float(sys.argv[1]))