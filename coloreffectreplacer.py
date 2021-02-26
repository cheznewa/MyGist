def addcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = min(vr+r,255)
 vg = min(vg+g,255)
 vb = min(vb+b,255)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def subcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = max(vr-r,0)
 vg = max(vg-g,0)
 vb = max(vb-b,0)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def xorcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = vr^r
 vg = vg^g
 vb = vb^b
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb
import sys
import string
while True:
 o = sys.stdin.read(1)
 if "#" == o:
  col = str(sys.stdin.read(6))
  if all(a in string.hexdigits for a in col):
   if sys.argv[1] == "add":
    col = addcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
   if sys.argv[1] == "sub":
    col = subcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
   if sys.argv[1] == "xor":
    col = xorcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
  sys.stdout.write("#")
  sys.stdout.write(col)
 else:
  sys.stdout.write(o)
 if not o:
  break
