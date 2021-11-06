import sys
from struct import unpack
min = int(sys.argv[1])
max = int(sys.argv[2])
fs = open("/dev/urandom","rb") 
no = 0
while True:
 o = sys.stdin.read(4)
 n = unpack("I",o)[0]
 if (n >= min) and (n < max):
  if sys.argv[3] == "16":
   a = int((65536.0*(n-min)/(float(max)-float(min))))
   p = int(a % 256)
   q = int(a / 256)
   sys.stdout.write("%s%s" %(chr(p),chr(q)))
   no = 0
  if sys.argv[3] == "8":
   i = int((256.0*(n-min)/(float(max)-float(min))))
   sys.stdout.write("%s" %(chr(i)))
   no = 0
 else:
  no = no + 1
  if no == int(sys.argv[4]):
   if sys.argv[3] == "16":
    sys.stdout.write(fs.read(2))
    no = 0
   if sys.argv[3] == "8":
    sys.stdout.write(fs.read(1))
    no = 0
