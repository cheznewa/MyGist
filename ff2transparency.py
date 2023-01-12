import sys
limit = int(sys.argv[1])
import os
if not "farbfeld" == sys.stdin.read(8):
 exit(1)
size = sys.stdin.read(8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
n = x*y
sys.stdout.write("farbfeld")
sys.stdout.write(size)
if not "farbfeld" == os.read(5,8): # Template
 exit(2)
size = os.read(5,8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
e = x*y
if not n == e:
 exit(3)
sys.stdout.write("farbfeld")
sys.stdout.write(size)
while n:
 o = sys.stdin.read(8)
 r = (ord(o[0])*256)+ord(o[1])
 g = (ord(o[2])*256)+ord(o[3])
 b = (ord(o[4])*256)+ord(o[5])
 oe = os.read(5,8)
 re = (ord(oe[0])*256)+ord(oe[1])
 ge = (ord(oe[2])*256)+ord(oe[3])
 be = (ord(oe[4])*256)+ord(oe[5])
 z = max(abs(r-re),abs(g-ge),abs(b-be))
 if z < limit:
  sys.stdout.write("%s%s%s%s%s%s%s%s" %(chr(r/256),chr(r%256),chr(g/256),chr(g%256),chr(b/256),chr(b%256),chr(0),chr(0)))
 else:
  sys.stdout.write("%s%s%s%s%s%s%s%s" %(chr(r/256),chr(r%256),chr(g/256),chr(g%256),chr(b/256),chr(b%256),o[6],o[7]))
 n=n-1