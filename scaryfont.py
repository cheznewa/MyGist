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
  nt = o.find("\"",ye+1)
  ne = o.find("\"",nt+1)
  nv = int(o[nt+1:ne])
  xv = xv+(((ord(r.read(1))-127)/255.0)*float(sys.argv[1]))
  yv = yv+(((ord(r.read(1))-127)/255.0)*float(sys.argv[1]))
  sys.stdout.write("<pt x=\"%s\" y=\"%s\" on=\"%s\"/>\n" %(xv,yv,nv))
 elif re.search("<delta ",o):
  nt = o.find("\"",1)
  ne = o.find("\"",nt+1)
  nv = int(o[nt+1:ne])
  xt = o.find("\"",ne+1)
  xe = o.find("\"",xt+1)
  xv = int(o[xt+1:xe])
  yt = o.find("\"",xe+1)
  ye = o.find("\"",yt+1)
  yv = int(o[yt+1:ye])
  xv = xv+(((ord(r.read(1))-127)/255.0)*float(sys.argv[1]))
  yv = yv+(((ord(r.read(1))-127)/255.0)*float(sys.argv[1]))
  sys.stdout.write("<delta pt=\"%s\" x=\"%s\" y=\"%s\"/>\n" %(nv,int(xv),int(yv)))
 else:
  sys.stdout.write(o)