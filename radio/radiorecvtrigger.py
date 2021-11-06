import sys
from struct import unpack
# BEGIN :: Trigger
fsa = open(sys.argv[1],"r")
ntrame = 0
nt = 0
params = fsa.readlines()
param = params[nt]
next =  int(param.split(";")[0])
min =  int(param.split(";")[1])
max =  int(param.split(";")[2])
# END   :: Trigger
while True:
 o = sys.stdin.read(4)
 n = unpack("I",o)[0]
 if next == ntrame:
  nt = nt + 1
  param = params[nt]
  next =  int(param.split(";")[0])
  min =  int(param.split(";")[1])
  max =  int(param.split(";")[2])
 if (n >= min) and (n < max):
  if sys.argv[2] == "16":
   a = int((65536.0*(n-min)/(float(max)-float(min))))
   p = int(a % 256)
   q = int(a / 256)
   sys.stdout.write("%s%s" %(chr(p),chr(q)))
  if sys.argv[2] == "8":
   i = int((65536.0*(n-min)/(float(max)-float(min))))
   sys.stdout.write("%s" %(chr(i)))
 ntrame = ntrame + 1