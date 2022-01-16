import sys
import re
xo = None
yo = None
r = open("/dev/urandom","rb")
for o in sys.stdin:
 if re.search("<pt ",o):
  xt = o.find("\"",1)
  xe = o.find("\"",xt+1)
  xv = int(o[xt+1:xe])
  yt = o.find("\"",xe+1)
  ye = o.find("\"",yt+1)
  yv = int(o[yt+1:ye])
  nt = re.search("on=",o)
  nv = int(filter(str.isdigit,o[nt.end():nt.end()+3]))
  xv = xv+(((ord(r.read(1))-127)/255.0)*float(sys.argv[1]))
  yv = yv+(((ord(r.read(1))-127)/255.0)*float(sys.argv[1]))
  sys.stdout.write("        <pt x=\"%s\" y=\"%s\" on=\"%s\"/>\n" %(xv,yv,nv))
 else:
  sys.stdout.write(o)