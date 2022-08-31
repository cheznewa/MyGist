import sys
if not "farbfeld" == sys.stdin.read(8):
 exit(1)
size = sys.stdin.read(8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
n = x*y
getb=0
getm=0
getc=0
gety=0
while bool(n):
 o = sys.stdin.read(8)
 r = (ord(o[0])*256)+ord(o[1])
 g = (ord(o[2])*256)+ord(o[3])
 b = (ord(o[4])*256)+ord(o[5])
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
 getb=getb+k
 getm=getm+m
 getc=getc+c
 gety=gety+y
 n=n-1

sys.stdout.write("K=%.10f\nC=%.10f\nM=%.10f\nY=%.10f\n" %(getb,getc,getm,gety))