import sys
from base58 import b58decode_int
min = int(sys.argv[1])
max = int(sys.argv[2])
fs = open("/dev/urandom","rb") 
no = 0
for o in sys.stdin:
 if int(b58decode_int(o)) >= min and int(b58decode_int(o)) < max:
  if sys.argv[3] == "16":
   a = int((65536.0*(int(b58decode_int(o))-min)/(float(max)-float(min))))
   p = int(a % 256)
   q = int(a / 256)
   sys.stdout.write("%s%s" %(chr(p),chr(q)))
   no = 0
  if sys.argv[3] == "8":
   i = int((256.0*(int(b58decode_int(o))-min)/(float(max)-float(min))))
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
