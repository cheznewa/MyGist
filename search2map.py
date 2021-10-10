import sys
def position2coordinate(p,b):
 pb = format(p,"0"+str(b*2)+"b")
 x = ""
 y = ""
 for n in range(b):
  x = x + pb[n*2]
  y = y + pb[1+n*2]
 return int(x,2),int(y,2)

o = sys.stdin.read(pow(2,int(sys.argv[1])*2))
p = 0
while True:
 p = o.find(sys.argv[2],p)
 if p == -1:
  break
 x,y = position2coordinate(p,int(sys.argv[1]))
 sys.stdout.write("<span style=\"position:absolute;left:%s;top:%s;\">X</span>\n" %(x,y))
 p = p + len(sys.argv[2])