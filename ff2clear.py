import sys
import math
mode = sys.argv[1]
if not "farbfeld" == sys.stdin.read(8):
 exit(1)
size = sys.stdin.read(8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
n = x*y
sys.stdout.write("farbfeld")
sys.stdout.write(size)
rr=0
gg=0
bb=0
if mode == "cc":
 ahe = sys.argv[2]
 bhe = sys.argv[3]
 ra = int(ahe[0:2],16)
 ga = int(ahe[2:4],16)
 ba = int(ahe[4:6],16)
 rb = int(bhe[0:2],16)
 gb = int(bhe[2:4],16)
 bc = int(bhe[4:6],16)
while bool(n):
 o = sys.stdin.read(8)
 r = (ord(o[0])*256)+ord(o[1])
 g = (ord(o[2])*256)+ord(o[3])
 b = (ord(o[4])*256)+ord(o[5])
 if not bool(n%x):
  rr=r
  gg=g
  bb=b
 dr=r-rr
 dg=g-gg
 db=b-bb
 rv=r
 gv=g
 bv=b
 d=(dr+dg+db)/3
 if mode == "rc":
  if d < 0:
   rv = min(r + abs(d),65535)
  elif d > 0:
   rv = max(r - abs(d),0)
 if mode == "gm":
  if d < 0:
   gv = min(g + abs(d),65535)
  elif d > 0:
   gv = max(g - abs(d),0)
 if mode == "by":
  if d < 0:
   bv = min(b + abs(d),65535)
  elif d > 0:
   bv = max(b - abs(d),0)
 if mode == "cr":
  if d < 0:
   gv = min(g + abs(d),65535)
   bv = min(b + abs(d),65535)
  elif d > 0:
   gv = max(g - abs(d),0)
   bv = max(b - abs(d),0)
 if mode == "mg":
  if d < 0:
   rv = min(r + abs(d),65535)
   bv = min(b + abs(d),65535)
  elif d > 0:
   rv = max(r - abs(d),0)
   bv = max(b - abs(d),0)
 if mode == "yb":
  if d < 0:
   rv = min(r + abs(d),65535)
   gv = min(g + abs(d),65535)
  elif d > 0:
   rv = max(r - abs(d),0)
   gv = max(g - abs(d),0)
 if mode == "cc":
  if d < 0:
   rv = min(r + (int((ra/255.0)*abs(d))),65535)
   gv = min(g + (int((ga/255.0)*abs(d))),65535)
   bv = min(b + (int((ba/255.0)*abs(d))),65535)
  elif d > 0:
   rv = max(r - (int((1-(rb/255.0))*(abs(d)))),0)
   gv = max(g - (int((1-(gb/255.0))*(abs(d)))),0)
   bv = max(b - (int((1-(bc/255.0))*(abs(d)))),0)
 if mode == "rgb":
  if d < 0:
   rv = min(r + int(65535*(math.sin(abs(d)/65535.0)*(math.pi*0.5))),65535)
   gv = min(g + int(65535*(math.sin(abs(d)/65535.0)*(math.pi*0.25))),65535)
   bv = min(b + int(65535*(math.sin(abs(d)/65535.0)*(math.pi*0.125))),65535)
  elif d > 0:
   rv = max(r - int(65535*(math.sin(abs(d)/65535.0)*(math.pi*0.5))),0)
   gv = max(g - int(65535*(math.sin(abs(d)/65535.0)*(math.pi*0.25))),0)
   bv = max(b - int(65535*(math.sin(abs(d)/65535.0)*(math.pi*0.125))),0)
 if mode == "bgr":
  if d < 0:
   rv = min(r + int(65535*(math.sin(abs(d)/65535.0)*(math.pi*0.125))),65535)
   gv = min(g + int(65535*(math.sin(abs(d)/65535.0)*(math.pi*0.25))),65535)
   bv = min(b + int(65535*(math.sin(abs(d)/65535.0)*(math.pi*0.5))),65535)
  elif d > 0:
   rv = max(r - int(65535*(math.sin(abs(d)/65535.0)*(math.pi*0.125))),0)
   gv = max(g - int(65535*(math.sin(abs(d)/65535.0)*(math.pi*0.25))),0)
   bv = max(b - int(65535*(math.sin(abs(d)/65535.0)*(math.pi*0.5))),0)
 sys.stdout.write("%s%s%s%s%s%s%s%s" %(chr(rv/256),chr(rv%256),chr(gv/256),chr(gv%256),chr(bv/256),chr(bv%256),o[6],o[7]))
 rr=r
 gg=g
 bb=b
 n=n-1