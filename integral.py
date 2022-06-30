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
 i=0
 an=0
 x=minint
 n=minint
 while x <= maxint:
  while n <= maxint:
   exec("u=" + formul)
   an=max(u,an)
   n=n+precis
  n=minint
  un=an*precis
  i=i+un
  x=x+precis
if modeop == "cap":
 x=minint
 n=minint
 mn=0
 mx=0
 while x <= maxint:
  while n <= maxint:
   exec("u=" + formul)
   mx=max(u,mx)
   mn=min(u,mn)
   n=n+precis
  un=(mx-mn)*precis
  i=i+un
  x=x+precis
  n=minint
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

sys.stdout.write("%s\n" %(i))