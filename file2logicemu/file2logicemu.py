import sys
import re
import math
fs = open(sys.argv[1],"rb")
c = fs.read()
l = len(c)
bits = math.log(l,2)
sys.stdout.write("0\"length : %s\"\n" %(l))
sys.stdout.write("  llllllll\n  ^^^^^^^^\n")
for o in range(l):
 b = str(bin(ord(c[o])))
 z = b[2:].zfill(8)
 a = re.sub("0","b",z)
 a = re.sub("1","B",a)
 if bits > o:
  sys.stdout.write("s>")
 else:
  sys.stdout.write("  ")
 sys.stdout.write(a)
 sys.stdout.write("\n")