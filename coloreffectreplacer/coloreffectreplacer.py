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

def bnwcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 base = (vr+vg+vb)/3
 vr = int(vr*float(1-(r/255.0)))+int(base*float(r/255.0))
 vg = int(vg*float(1-(g/255.0)))+int(base*float(g/255.0))
 vb = int(vb*float(1-(b/255.0)))+int(base*float(b/255.0))
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def sepcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 baser = (vr+vg+vb)/3
 baseg = (vr+vg+vb)/4
 baseb = (vr+vg)/6
 vr = int(vr*float(1-(r/255.0)))+int(baser*float(r/255.0))
 vg = int(vg*float(1-(g/255.0)))+int(baseg*float(g/255.0))
 vb = int(vb*float(1-(b/255.0)))+int(baseb*float(b/255.0))
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def rmpcol(col,a,b,f):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 ar = int(a[0:2],16)
 ag = int(a[2:4],16)
 ab = int(a[4:6],16)
 br = int(b[0:2],16)
 bg = int(b[2:4],16)
 bb = int(b[4:6],16)
 z = float(max(f-(abs(vr-ar)+abs(vg-ag)+abs(vb-ab)),0))
 vr = int(vr*float(1-(z/f)))+int(br*float(z/f))
 vg = int(vg*float(1-(z/f)))+int(bg*float(z/f))
 vb = int(vb*float(1-(z/f)))+int(bb*float(z/f))
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

i = open("/dev/urandom","rb")
def rndcol(col,a,f):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 ar = int(a[0:2],16)
 ag = int(a[2:4],16)
 ab = int(a[4:6],16)
 br = ord(i.read(1))
 bg = ord(i.read(1))
 bb = ord(i.read(1))
 z = float(max(f-(abs(vr-ar)+abs(vg-ag)+abs(vb-ab)),0))
 vr = int(vr*float(1-(z/f)))+int(br*float(z/f))
 vg = int(vg*float(1-(z/f)))+int(bg*float(z/f))
 vb = int(vb*float(1-(z/f)))+int(bb*float(z/f))
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def powcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = pow(vr,r,256)
 vg = pow(vg,g,256)
 vb = pow(vb,b,256)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def expcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = pow(r,vr,256)
 vg = pow(g,vg,256)
 vb = pow(b,vb,256)
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
   if sys.argv[1] == "bnw":
    col = bnwcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
   if sys.argv[1] == "sep":
    col = sepcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
   if sys.argv[1] == "rmp":
    col = rmpcol(col,sys.argv[2],sys.argv[3],int(sys.argv[4]))
   if sys.argv[1] == "rnd":
    col = rndcol(col,sys.argv[2],int(sys.argv[3]))
   if sys.argv[1] == "pow":
    col = powcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
   if sys.argv[1] == "exp":
    col = expcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
  sys.stdout.write("#")
  sys.stdout.write(col)
 else:
  sys.stdout.write(o)
 if not o:
  break
