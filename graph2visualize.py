import sys
def position2coordinate(p,b):
 pb = format(p,"0"+str(b*2)+"b")
 x = ""
 y = ""
 for n in range(b):
  x = x + pb[1+n*2]
  y = y + pb[n*2]
 return int(x,2),int(y,2)

sys.stdout.write("<svg width=\"%s\" height=\"%s\" viewbox=\"0 0 %s %s\" xmlns=\"http://www.w3.org/2000/svg\">\n" %(5+pow(2,int(sys.argv[1]))*int(sys.argv[3]),5+pow(2,int(sys.argv[1]))*int(sys.argv[3]),5+pow(2,int(sys.argv[1]))*int(sys.argv[3]),5+pow(2,int(sys.argv[1]))*int(sys.argv[3])))
for o in sys.stdin:
 n = o.split()
 if sys.argv[2] == "bip":
  ax,ay = position2coordinate(int(n[0])*2,int(sys.argv[1]))
  bx,by = position2coordinate(1+int(n[1])*2,int(sys.argv[1]))
 elif sys.argv[2] == "dir":
  ax,ay = position2coordinate(int(n[0]),int(sys.argv[1]))
  bx,by = position2coordinate(int(n[1]),int(sys.argv[1]))
 sys.stdout.write("<line x1=\"%s\" y1=\"%s\" x2=\"%s\" y2=\"%s\" stroke=\"black\"/>\n" %(ax*int(sys.argv[3]),ay*int(sys.argv[3]),bx*int(sys.argv[3]),by*int(sys.argv[3])))

sys.stdout.write("</svg>\n")