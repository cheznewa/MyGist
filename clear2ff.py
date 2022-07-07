import sys
mode = sys.argv[1]
if not "farbfeld" == sys.stdin.read(8):
 exit(1)
size = sys.stdin.read(8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
n = x*y
sys.stdout.write("farbfeld")
sys.stdout.write(size)
while bool(n):
 o = sys.stdin.read(8)
 r = (ord(o[0])*256)+ord(o[1])
 g = (ord(o[2])*256)+ord(o[3])
 b = (ord(o[4])*256)+ord(o[5])
 rv=r
 gv=g
 bv=b
 if mode == "rc":
  d=r-((g+b)/2)
  if d < 0:
   rv = min(r + abs(d),65535)
  elif d > 0:
   rv = max(r - abs(d),0)
 if mode == "gm":
  d=g-((r+b)/2)
  if d < 0:
   gv = min(g + abs(d),65535)
  elif d > 0:
   gv = max(g - abs(d),0)
 if mode == "by":
  d=b-((r+g)/2)
  if d < 0:
   bv = min(b + abs(d),65535)
  elif d > 0:
   bv = max(b - abs(d),0)
 if mode == "cr":
  d=((g+b)/2)-r
  if d < 0:
   gv = min(g + abs(d),65535)
   bv = min(b + abs(d),65535)
  elif d > 0:
   gv = max(g - abs(d),0)
   bv = max(b - abs(d),0)
 if mode == "mg":
  d=((r+b)/2)-g
  if d < 0:
   rv = min(r + abs(d),65535)
   bv = min(b + abs(d),65535)
  elif d > 0:
   rv = max(r - abs(d),0)
   bv = max(b - abs(d),0)
 if mode == "yb":
  d=((r+g)/2)-b
  if d < 0:
   rv = min(r + abs(d),65535)
   gv = min(g + abs(d),65535)
  elif d > 0:
   rv = max(r - abs(d),0)
   gv = max(g - abs(d),0)
 sys.stdout.write("%s%s%s%s%s%s%s%s" %(chr(rv/256),chr(rv%256),chr(gv/256),chr(gv%256),chr(bv/256),chr(bv%256),o[6],o[7]))
 n=n-1