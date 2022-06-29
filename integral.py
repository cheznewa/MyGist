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
if modeop == "cup":
 i=0
 u=0
 x=minint
 n=minint
 while x <= maxint:
  while n <= maxint:
   uu=u
   exec("u=" + formul)
   u=max(u,uu)
   n=n+precis
  i=i+u
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
   un=mx-mn
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
  u=(u-uu)/(1/precis)
  x=x+precis
  i=i+u
if modeop == "crb":
 i=0
 u=0
 x=minint
 while x <= maxint:
  uu=u
  exec("u=" + formul)
  u=abs((u-uu)/(1/precis))
  x=x+precis
  i=i+u


sys.stdout.write("%s\n" %(i))