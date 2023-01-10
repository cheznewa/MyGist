# Usage :::::: python2 paperbackground.py 5< background.ff < paper.ff
import sys
import os
if not "farbfeld" == sys.stdin.read(8):
 exit(1)
size = sys.stdin.read(8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
n = x*y
sys.stdout.write("farbfeld")
sys.stdout.write(size)
if not "farbfeld" == os.read(5,8): # Background
 exit(2)
size = os.read(5,8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
e = x*y
if not n == e:
 exit(3)
while bool(n):
 o = sys.stdin.read(8)
 r = (ord(o[0])*256)+ord(o[1])
 g = (ord(o[2])*256)+ord(o[3])
 b = (ord(o[4])*256)+ord(o[5])
 oe = os.read(5,8)
 re = (ord(oe[0])*256)+ord(oe[1])
 ge = (ord(oe[2])*256)+ord(oe[3])
 be = (ord(oe[4])*256)+ord(oe[5])
# Source From ::::::: https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
 k = 1-max((r/65535.0),(g/65535.0),(b/65535.0))
 if not k == 1.0:
  c = (1-(r/65535.0)-k)/(1-k)
  m = (1-(g/65535.0)-k)/(1-k)
  y = (1-(b/65535.0)-k)/(1-k)
 else:
  c = 0
  m = 0
  y = 0
 # End Source
 z = max(int(k*65535),int(c*65535),int(m*65535),int(y*65535))
 r = max(r-int((65535-re)*((65535-z)/65535.0)),0)
 g = max(g-int((65535-ge)*((65535-z)/65535.0)),0)
 b = max(b-int((65535-be)*((65535-z)/65535.0)),0)
 sys.stdout.write("%s%s%s%s%s%s%s%s" %(chr(r/256),chr(r%256),chr(g/256),chr(g%256),chr(b/256),chr(b%256),o[6],o[7]))
 n=n-1