import sys
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
rm=0
gm=0
bm=0

while bool(n):
 o = sys.stdin.read(8)
 r = (ord(o[0])*256)+ord(o[1])
 g = (ord(o[2])*256)+ord(o[3])
 b = (ord(o[4])*256)+ord(o[5])
 if not bool(n%x):
  rr=r
  gg=g
  bb=b
 dr=abs(r-rr)
 dg=abs(g-gg)
 db=abs(b-bb)
 rv=r
 gv=g
 bv=b
 d=max(dr,dg,db)
 if d < 21845 or d > 43691:
  rv = r
  gv = g
  bv = b
  rm = rv
  gm = gv
  bm = bv
 else:
  rv = rm
  gv = gm
  bv = bm
 sys.stdout.write("%s%s%s%s%s%s%s%s" %(chr(rv/256),chr(rv%256),chr(gv/256),chr(gv%256),chr(bv/256),chr(bv%256),o[6],o[7]))
 rr=r
 gg=g
 bb=b
 n=n-1