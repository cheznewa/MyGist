import sys
from math import *
modeop=sys.argv[1]
precis=float(sys.argv[2])
minint=float(sys.argv[3])
maxint=float(sys.argv[4])
formul=sys.argv[5]
i=0
if modeop == "int":
 x=minint
 while x <= maxint:
  exec("u=" + formul)
  u=u*precis
  x=x+precis
  i=i+u
if modeop == "in2":
 x=minint
 y=minint
 while x <= maxint:
  while y <= maxint:
   exec("u=" + formul)
   u=u*pow(precis,2)
   y=y+precis
   i=i+u
  y=minint
  x=x+precis
if modeop == "in3":
 x=minint
 y=minint
 z=minint
 while x <= maxint:
  while y <= maxint:
   while z <= maxint:
    exec("u=" + formul)
    u=u*pow(precis,3)
    z=z+precis
    i=i+u
   z=minint
   y=y+precis
  y=minint
  x=x+precis
if modeop == "in4":
 x=minint
 y=minint
 z=minint
 w=minint
 while x <= maxint:
  while y <= maxint:
   while z <= maxint:
    while w <= maxint:
     exec("u=" + formul)
     u=u*pow(precis,4)
     w=w+precis
     i=i+u
    w=minint
    z=z+precis
   z=minint
   y=y+precis
  y=minint
  x=x+precis
if modeop == "cup":
 x=minint
 n=minint
 an=None
 while x <= maxint:
  while n <= maxint:
   exec("u=" + formul)
   if not an:
    an=u
   an=max(u,an)
   n=n+precis
  un=an*precis
  i=i+un
  x=x+precis
  n=minint
  an=None
if modeop == "cap":
 x=minint
 n=minint
 mx=None
 mn=None
 while x <= maxint:
  while n <= maxint:
   exec("u=" + formul)
   if not mx:
    mx=u
   if not mn:
    mn=u
   mx=max(u,mx)
   mn=min(u,mn)
   n=n+precis
  un=(mx-mn)*precis
  i=i+un
  x=x+precis
  n=minint
  mx=None
  mn=None
if modeop == "crm":
 u=0
 x=minint
 while x <= maxint:
  uu=u
  exec("u=" + formul)
  un=u-uu
  x=x+precis
  i=i+un
if modeop == "crb":
 u=0
 x=minint
 while x <= maxint:
  uu=u
  exec("u=" + formul)
  un=abs(u-uu)
  x=x+precis
  i=i+un
if modeop == "mul":
 u=0
 x=minint
 n=minint
 while x <= maxint:
  while n <= maxint:
   uu=u
   exec("u=" + formul)
   un=u*uu
   n=n+precis
   i=i+(un*pow(precis,2))
  x=x+precis
  n=minint
if modeop == "add":
 u=0
 x=minint
 n=minint
 while x <= maxint:
  while n <= maxint:
   uu=u
   exec("u=" + formul)
   un=u+uu
   n=n+precis
   i=i+(un*pow(precis,2))
  x=x+precis
  n=minint
if modeop == "atn":
 x=minint
 while x <= maxint:
  exec("u=" + formul)
  u=atan(u)
  x=x+precis
  i=i+u
 i=i/((maxint-minint)*(1/precis))
if modeop == "min":
 u=0
 x=minint
 n=minint
 while x <= maxint:
  while n <= maxint:
   uu=u
   exec("u=" + formul)
   un=min(u,uu)
   n=n+precis
   i=i+(un*pow(precis,2))
  x=x+precis
  n=minint
if modeop == "max":
 u=0
 x=minint
 n=minint
 while x <= maxint:
  while n <= maxint:
   uu=u
   exec("u=" + formul)
   un=max(u,uu)
   n=n+precis
   i=i+(un*pow(precis,2))
  x=x+precis
  n=minint
if modeop == "med":
 u=0
 x=minint
 n=minint
 while x <= maxint:
  while n <= maxint:
   uu=u
   exec("u=" + formul)
   un=(u+uu)/2
   n=n+precis
   i=i+(un*pow(precis,2))
  x=x+precis
  n=minint
if modeop == "if2":
 x=minint
 y=minint
 while x <= maxint:
  while y <= maxint:
   exec("u=" + formul)
   if u < 0:
    i=i+pow(precis,2)
   y=y+precis
  y=minint
  x=x+precis
if modeop == "sp2":
 x=minint
 y=minint
 while x <= maxint:
  while y <= maxint:
   exec("u=" + formul)
   if u > 0:
    i=i+pow(precis,2)
   y=y+precis
  y=minint
  x=x+precis
if modeop == "inf":
 x=minint
 while x <= maxint:
  exec("u=" + formul)
  if u < 0:
   i=i+precis
  x=x+precis
if modeop == "sup":
 x=minint
 while x <= maxint:
  exec("u=" + formul)
  if u > 0:
   i=i+precis
  x=x+precis
if modeop == "rnd":
 fs = open("/dev/urandom","rb")
 x=minint
 while x <= maxint:
  exec("u=" + formul)
  rnd = fs.read(4)
  grd = (ord(rnd[0])*pow(256,-1))+(ord(rnd[1])*pow(256,-2))+(ord(rnd[2])*pow(256,-3))+(ord(rnd[3])*pow(256,-4))
  u=u*grd
  u=u*precis
  x=x+precis
  i=i+u
if modeop == "rd2":
 fs = open("/dev/urandom","rb")
 x=minint
 y=minint
 while x <= maxint:
  while y <= maxint:
   exec("u=" + formul)
   rnd = fs.read(4)
   grd = (ord(rnd[0])*pow(256,-1))+(ord(rnd[1])*pow(256,-2))+(ord(rnd[2])*pow(256,-3))+(ord(rnd[3])*pow(256,-4))
   u=u*grd
   u=u*pow(precis,2)
   y=y+precis
   i=i+u
  y=minint
  x=x+precis
if modeop == "rd3":
 fs = open("/dev/urandom","rb")
 x=minint
 y=minint
 z=minint
 while x <= maxint:
  while y <= maxint:
   while z <= maxint:
    exec("u=" + formul)
    u=u*pow(precis,3)
    rnd = fs.read(4)
    grd = (ord(rnd[0])*pow(256,-1))+(ord(rnd[1])*pow(256,-2))+(ord(rnd[2])*pow(256,-3))+(ord(rnd[3])*pow(256,-4))
    u=u*grd
    z=z+precis
    i=i+u
   z=minint
   y=y+precis
  y=minint
  x=x+precis
if modeop == "rd4":
 fs = open("/dev/urandom","rb")
 x=minint
 y=minint
 z=minint
 w=minint
 while x <= maxint:
  while y <= maxint:
   while z <= maxint:
    while w <= maxint:
     exec("u=" + formul)
     rnd = fs.read(4)
     grd = (ord(rnd[0])*pow(256,-1))+(ord(rnd[1])*pow(256,-2))+(ord(rnd[2])*pow(256,-3))+(ord(rnd[3])*pow(256,-4))
     u=u*grd
     u=u*pow(precis,4)
     w=w+precis
     i=i+u
    w=minint
    z=z+precis
   z=minint
   y=y+precis
  y=minint
  x=x+precis
sys.stdout.write("%s\n" %(i))