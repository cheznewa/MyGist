import sys
def coordinate2position(c,b):
 xb = format(c[0],"0"+str(b)+"b")
 yb = format(c[1],"0"+str(b)+"b")
 g = ""
 for n in range(b):
  g = g + yb[n] + xb[n]
 return int(g,2)

o = sys.stdin.readlines()
for n in range(pow(pow(2,int(sys.argv[1])),2)):
 p = coordinate2position([n%pow(2,int(sys.argv[1])),n/pow(2,int(sys.argv[1]))],int(sys.argv[1]))
 sys.stdout.write(o[p].rstrip("\n"))
 if (pow(2,int(sys.argv[1]))-1) == (n%pow(2,int(sys.argv[1]))):
  sys.stdout.write("\n")
 else:
  sys.stdout.write(sys.argv[2])