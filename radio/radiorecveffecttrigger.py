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
fs = open("/dev/urandom","rb")
if not((sys.argv[5] == "beep") or (sys.argv[5] == "noise")):
 fsf = open(sys.argv[5],"rb")
no = 0
f = 0
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
   no = 0
  if sys.argv[2] == "8":
   i = int((256.0*(n-min)/(float(max)-float(min))))
   sys.stdout.write("%s" %(chr(i)))
   no = 0
 else:
  no = no + 1
  if no == int(sys.argv[3]):
   if sys.argv[2] == "16":
    if sys.argv[5] == "beep":
     sys.stdout.write("%s%s" %(chr(((f/50)%2)*255),chr(((f/50)%2)*255)))
     f = (f + 1) % 100
    elif sys.argv[5] == "noise":
     sys.stdout.write(fs.read(2))
    else:
     sys.stdout.write(fsf.read(2))
    no = 0
   if sys.argv[3] == "8":
    if sys.argv[5] == "beep":
     sys.stdout.write("%s" %(chr(((f/50)%2)*255)))
     f = (f + 1) % 100
    elif sys.argv[5] == "noise":
     sys.stdout.write(fs.read(1))
    else:
     sys.stdout.write(fsf.read(1))
    no = 0
 ntrame = ntrame + 1
 if n == max-1:
  sys.stderr.write("\x07")