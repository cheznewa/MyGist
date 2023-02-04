import sys
import math
if not "farbfeld" == sys.stdin.read(8):
 exit(1)
size = sys.stdin.read(8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
n = x*y
m = n
sys.stdout.write("farbfeld")
sys.stdout.write(size)
while bool(n):
 e = m-n
 o = sys.stdin.read(8)
 r = (ord(o[0])*256)+ord(o[1])
 g = (ord(o[2])*256)+ord(o[3])
 b = (ord(o[4])*256)+ord(o[5])
 a = e%x
 z = e/x
 sr = int(65535*(a/float(x)))
 sg = int(65535*(z/float(y)))
 sb = 65535-int(65535*(a/float(x)))
 rv = min(max(r+(sr-32767),0),65535)
 gv = min(max(g+(sg-32767),0),65535)
 bv = min(max(b+(sb-32767),0),65535)
 sys.stdout.write("%s%s%s%s%s%s%s%s" %(chr(rv/256),chr(rv%256),chr(gv/256),chr(gv%256),chr(bv/256),chr(bv%256),o[6],o[7]))
 n=n-1