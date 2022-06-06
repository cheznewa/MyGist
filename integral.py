import sys
from math import *
precis=float(sys.argv[1])
minint=float(sys.argv[2])
maxint=float(sys.argv[3])
formul=sys.argv[4]
i=0
x=minint
while x <= maxint:
 exec("u=" + formul)
 u=u*precis
 x=x+precis
 i=i+u

sys.stdout.write("%s\n" %(i))