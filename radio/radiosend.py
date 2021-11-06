import sys
from struct import pack
min = int(sys.argv[1])
max = int(sys.argv[2])
if sys.argv[3] == "16":
 while True:
  o = sys.stdin.read(2)
  sys.stdout.write("%s" %(pack("I",(int(((ord(o[0])/65536.0)+(ord(o[1])/256.0))*(max-min))+min))))
if sys.argv[3] == "8":
 while True:
  o = sys.stdin.read(1)
  sys.stdout.write("%s" %(pack("I",int((ord(o)/256.0)*(max-min))+min)))