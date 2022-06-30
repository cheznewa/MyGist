import sys
from math import *
modeop=sys.argv[1]
precis=float(sys.argv[2])
minint=float(sys.argv[3])
maxint=float(sys.argv[4])
formul=sys.argv[5]
if modeop == "int":
 i=0
 x=minint
 while x <= maxint:
  exec("u=" + formul)
  u=u*precis
  x=x+precis
  i=i+u
if modeop == "in2":
 i=0
 x=minint
 y=minint
 precis=pow(precis,0.5)
 while x <= maxint:
  while y <= maxint:
   exec("u=" + formul)
   u=u*precis
   y=y+precis
   i=i+u
  x=x+precis
if modeop == "in3":
 i=0
 x=minint
 y=minint
 z=minint
 precis=pow(precis,1/3.0)
 while x <= maxint:
  while y <= maxint:
   while z <= maxint:
    exec("u=" + formul)
    u=u*precis
    z=z+precis
    i=i+u
   y=y+precis
  x=x+precis
if modeop == "in4":
 i=0
 x=minint
 y=minint
 z=minint
 w=minint
 precis=pow(precis,0.25)
 while x <= maxint:
  while y <= maxint:
   while z <= maxint:
    while w <= maxint:
     exec("u=" + formul)
     u=u*precis
     w=w+precis
     i=i+u
    z=z+precis
   y=y+precis
  x=x+precis
if modeop == "cup":
 i=0
 u=0
 x=minint
 n=minint
 while x <= maxint:
  while n <= maxint:
   uu=u
   exec("u=" + formul)
   un=max(u,uu)*precis
   n=n+precis
  i=i+un
  x=x+precis
if modeop == "cap":
 i=0
 u=0
 x=minint
 n=minint
 while x <= maxint:
  while n <= maxint:
   uu=u
   exec("u=" + formul)
   mx=max(u,uu)
   mn=min(u,uu)
   un=(mx-mn)*precis
   n=n+precis
  i=i+un
  x=x+precis
if modeop == "crm":
 i=0
 u=0
 x=minint
 while x <= maxint:
  uu=u
  exec("u=" + formul)
  un=u-uu
  x=x+precis
  i=i+un
if modeop == "crb":
 i=0
 u=0
 x=minint
 while x <= maxint:
  uu=u
  exec("u=" + formul)
  un=abs(u-uu)
  x=x+precis
  i=i+un
if modeop == "mul":
 i=0
 u=0
 x=minint
 n=minint
 while x <= maxint:
  while n <= maxint:
   uu=u
   exec("u=" + formul)
   un=(u*uu)*precis
   n=n+precis
  i=i+un
  x=x+precis
if modeop == "add":
 i=0
 u=0
 x=minint
 n=minint
 while x <= maxint:
  while n <= maxint:
   uu=u
   exec("u=" + formul)
   un=(u+uu)*precis
   n=n+precis
  i=i+un
  x=x+precis
if modeop == "atn":
 i=0
 x=minint
 while x <= maxint:
  exec("u=" + formul)
  u=atan(u)
  x=x+precis
  i=i+u
 i=i/((maxint-minint)*(1/precis))

sys.stdout.write("%s\n" %(i))