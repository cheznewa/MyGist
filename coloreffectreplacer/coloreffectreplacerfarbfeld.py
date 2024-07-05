def addcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = min(vr+r,255)
 vg = min(vg+g,255)
 vb = min(vb+b,255)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def subcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = max(vr-r,0)
 vg = max(vg-g,0)
 vb = max(vb-b,0)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def xorcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = vr^r
 vg = vg^g
 vb = vb^b
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def bnwcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 base = (vr+vg+vb)/3
 vr = max(min(int(vr*float(1-(r/255.0)))+int(base*float(r/255.0)),255),0)
 vg = max(min(int(vg*float(1-(g/255.0)))+int(base*float(g/255.0)),255),0)
 vb = max(min(int(vb*float(1-(b/255.0)))+int(base*float(b/255.0)),255),0)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def sepcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 baser = (vr+vg+vb)/3
 baseg = (vr+vg+vb)/4
 baseb = (vr+vg)/6
 vr = int(vr*float(1-(r/255.0)))+int(baser*float(r/255.0))
 vg = int(vg*float(1-(g/255.0)))+int(baseg*float(g/255.0))
 vb = int(vb*float(1-(b/255.0)))+int(baseb*float(b/255.0))
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def rmpcol(col,a,b,f):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 ar = int(a[0:2],16)
 ag = int(a[2:4],16)
 ab = int(a[4:6],16)
 br = int(b[0:2],16)
 bg = int(b[2:4],16)
 bb = int(b[4:6],16)
 z = float(max(f-(abs(vr-ar)+abs(vg-ag)+abs(vb-ab)),0))
 vr = int(vr*float(1-(z/f)))+int(br*float(z/f))
 vg = int(vg*float(1-(z/f)))+int(bg*float(z/f))
 vb = int(vb*float(1-(z/f)))+int(bb*float(z/f))
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

i = open("/dev/urandom","rb")
def rndcol(col,a,f):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 ar = int(a[0:2],16)
 ag = int(a[2:4],16)
 ab = int(a[4:6],16)
 br = ord(i.read(1))
 bg = ord(i.read(1))
 bb = ord(i.read(1))
 z = float(max(f-(abs(vr-ar)+abs(vg-ag)+abs(vb-ab)),0))
 vr = int(vr*float(1-(z/f)))+int(br*float(z/f))
 vg = int(vg*float(1-(z/f)))+int(bg*float(z/f))
 vb = int(vb*float(1-(z/f)))+int(bb*float(z/f))
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def powcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = pow(vr,r,256)
 vg = pow(vg,g,256)
 vb = pow(vb,b,256)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def expcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = pow(r,vr,256)
 vg = pow(g,vg,256)
 vb = pow(b,vb,256)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def mapcol(col,gpl):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 z = []
 l = len(gpl)
 for cgpl in gpl:
  ar = int(cgpl[0:2],16)
  ag = int(cgpl[2:4],16)
  ab = int(cgpl[4:6],16)
  z.append(max(abs(vr-ar)+abs(vg-ag)+abs(vb-ab),0))
 d = 10000
 rcol = "000000"
 for n in range(l):
  if z[n] < d:
   d = z[n]
   rcol = gpl[n]
 return rcol

def unicol(col,base):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 br = int(base[0:2],16)
 bg = int(base[2:4],16)
 bb = int(base[4:6],16)
 base = (vr+vg+vb)/3
 vr = int(base*(br/255.0))
 vg = int(base*(bg/255.0))
 vb = int(base*(bb/255.0))
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def colcol(col,base,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 br = int(base[0:2],16)
 bg = int(base[2:4],16)
 bb = int(base[4:6],16)
 vr = int(vr*float(1-(r/255.0)))+int(br*float(r/255.0))
 vg = int(vg*float(1-(g/255.0)))+int(bg*float(g/255.0))
 vb = int(vb*float(1-(b/255.0)))+int(bb*float(b/255.0))
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def poscol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = (vr/int(255.0/r))*int(255.0/r)
 vg = (vg/int(255.0/g))*int(255.0/g)
 vb = (vb/int(255.0/b))*int(255.0/b)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def empcol(col,gpl):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 z = []
 l = len(gpl)
 for cgpl in gpl:
  ar = int(cgpl[0:2],16)
  ag = int(cgpl[2:4],16)
  ab = int(cgpl[4:6],16)
  z.append(max(abs(vr-ar)+abs(vg-ag)+abs(vb-ab),0))
 d = 10000
 rcol = "000000"
 ll = int(255.0/l)
 for n in range(l):
  if z[n] < d:
   d = z[n]
   r = n*ll
 re = str(format(r,"02x"))
 return re + re + re

def dmpcol(col,gpl):
 gr = int(col[0:2],16)
 l = len(gpl)
 rcol = gpl[gr/int(255.0/l)]
 return rcol

def gamcol(col,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = int(pow(vr/255.0,1.0/r)*255)
 vg = int(pow(vg/255.0,1.0/g)*255)
 vb = int(pow(vb/255.0,1.0/b)*255)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb
 
def shucol(col,rg,rb,gr,gb,br,bg):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 fr = min(((int(vr*float((255-rg)/255.0))+int(vr*float((255-rb)/255.0)))/2)+((int(vg*float((gr)/255.0))+int(vb*float((br)/255.0)))/2),255)
 fg = min(((int(vg*float((255-gr)/255.0))+int(vg*float((255-gb)/255.0)))/2)+((int(vr*float((rg)/255.0))+int(vb*float((bg)/255.0)))/2),255)
 fb = min(((int(vb*float((255-br)/255.0))+int(vb*float((255-bg)/255.0)))/2)+((int(vr*float((rb)/255.0))+int(vg*float((gb)/255.0)))/2),255)
 vr = str(format(fr,"02x"))
 vg = str(format(fg,"02x"))
 vb = str(format(fb,"02x"))
 return vr + vg + vb
 
from time import time
def oldcol(col,t,l):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 base = (vr+vg+vb)/3
 t = min((int(time())-t)/l,511)
 if t < 256:
  vr = int(vr*float(1-(t/255.0)))+int(base*float(t/255.0))
  vg = int(vg*float(1-(t/255.0)))+int(base*float(t/255.0))
  vb = int(vb*float(1-(t/255.0)))+int(base*float(t/255.0))
 else:
  vr = (base/int(255.0/float(255-(t-255))))*int(255.0/float(255-(t-255)))
  vg = (base/int(255.0/float(255-(t-255))))*int(255.0/float(255-(t-255)))
  vb = (base/int(255.0/float(255-(t-255))))*int(255.0/float(255-(t-255)))
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def depcol(col,bfar,bclose):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 ar = int(bfar[0:2],16)
 ag = int(bfar[2:4],16)
 ab = int(bfar[4:6],16)
 br = int(bclose[0:2],16)
 bg = int(bclose[2:4],16)
 bb = int(bclose[4:6],16)
 aa = max(abs(vr-ar)+abs(vg-ag)+abs(vb-ab),0)
 bb = max(abs(vr-br)+abs(vg-bg)+abs(vb-bb),0)
 cc = max((aa-bb)/3,0)
 vr = str(format(cc,"02x"))
 return vr + vr + vr

def pprcol(col,h): # Paper Color
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 hr = int(h[0:2],16)
 hg = int(h[2:4],16)
 hb = int(h[4:6],16)
 # Source From ::::::: https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
 k = 1-max((vr/255.0),(vg/255.0),(vb/255.0))
 if not k == 1.0:
  c = (1-(vr/255.0)-k)/(1-k)
  m = (1-(vg/255.0)-k)/(1-k)
  y = (1-(vb/255.0)-k)/(1-k)
 else:
  c = 0
  m = 0
  y = 0
 # End Source
 z = max(int(k*255),int(c*255),int(m*255),int(y*255))
 vr = max(vr-int((255-hr)*((255-z)/255.0)),0)
 vg = max(vg-int((255-hg)*((255-z)/255.0)),0)
 vb = max(vb-int((255-hb)*((255-z)/255.0)),0)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

from math import *
def intcol(col,p,fr,fg,fb): # Integral
 br = int(col[0:2],16)
 bg = int(col[2:4],16)
 bb = int(col[4:6],16)
 x=0
 vr=0
 vg=0
 vb=0
 while x <= br:
  exec("u=" + fr)
  u=u*p
  x=x+p
  vr=vr+u
 x=0
 while x <= bg:
  exec("u=" + fg)
  u=u*p
  x=x+p
  vg=vg+u
 x=0
 while x <= bb:
  exec("u=" + fb)
  u=u*p
  x=x+p
  vb=vb+u
 vr = str(format(min(max(int(vr),0),255),"02x"))
 vg = str(format(min(max(int(vg),0),255),"02x"))
 vb = str(format(min(max(int(vb),0),255),"02x"))
 return vr + vg + vb

def funcol(col,fr,fg,fb): # Function/Custom
 r = float(int(col[0:2],16))
 g = float(int(col[2:4],16))
 b = float(int(col[4:6],16))
 exec("u=" + fr)
 vr = int(u%256)
 exec("u=" + fg)
 vg = int(u%256)
 exec("u=" + fb)
 vb = int(u%256)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def lumcol(col,sr,sg,sb,r,g,b):
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = int(max(min(vr+(r*(vr-sr)),255),0))
 vg = int(max(min(vg+(g*(vg-sg)),255),0))
 vb = int(max(min(vb+(b*(vb-sb)),255),0))
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def iprcol(col,h,i): # Invert Paper Color
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 hr = int(h[0:2],16)
 hg = int(h[2:4],16)
 hb = int(h[4:6],16)
 ir = int(i[0:2],16)
 ig = int(i[2:4],16)
 ib = int(i[4:6],16)
 # Source From ::::::: https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
 k = 1-max((vr/255.0),(vg/255.0),(vb/255.0))
 if not k == 1.0:
  c = (1-(vr/255.0)-k)/(1-k)
  m = (1-(vg/255.0)-k)/(1-k)
  y = (1-(vb/255.0)-k)/(1-k)
 else:
  c = 0
  m = 0
  y = 0
 # End Source
 z = max(int(k*255),int(c*255),int(m*255),int(y*255))
 vr = max(int(k*ir)+vr-int((255-hr)*((255-z)/255.0)),0)
 vg = max(int(k*ig)+vg-int((255-hg)*((255-z)/255.0)),0)
 vb = max(int(k*ib)+vb-int((255-hb)*((255-z)/255.0)),0)
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

def dprcol(col,vk,vc,vm,vy): # Deficiency Printing 
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 # Source From ::::::: https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
 k = 1-max((vr/255.0),(vg/255.0),(vb/255.0))
 if not k == 1.0:
  c = (1-(vr/255.0)-k)/(1-k)
  m = (1-(vg/255.0)-k)/(1-k)
  y = (1-(vb/255.0)-k)/(1-k)
 else:
  c = 0
  m = 0
  y = 0
  # End Source
 k = (int(vk)/255.0)*k
 c = (int(vc)/255.0)*c
 m = (int(vm)/255.0)*m
 y = (int(vy)/255.0)*y
 # Source From ::::::: https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
 r = (1-c)*(1-k)
 g = (1-m)*(1-k)
 b = (1-y)*(1-k)
 # End Source
 vr = str(format(int(r*255),"02x"))
 vg = str(format(int(g*255),"02x"))
 vb = str(format(int(b*255),"02x"))
 return vr + vg + vb

def thtcol(col,r,g,b): # Theta Lumineux
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 vr = int(min(vr*r,255))
 vg = int(min(vg*g,255))
 vb = int(min(vb*b,255))
 vr = str(format(vr,"02x"))
 vg = str(format(vg,"02x"))
 vb = str(format(vb,"02x"))
 return vr + vg + vb

import sys
if not "farbfeld" == sys.stdin.read(8):
 exit(1)
size = sys.stdin.read(8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
n = x*y
sys.stdout.write("farbfeld")
sys.stdout.write(size)
while bool(n):
 o = sys.stdin.read(8)
 acol = str(format(ord(o[0]),"02x")) + str(format(ord(o[2]),"02x")) + str(format(ord(o[4]),"02x"))
 bcol = str(format(ord(o[1]),"02x")) + str(format(ord(o[3]),"02x")) + str(format(ord(o[5]),"02x"))
 if sys.argv[1] == "add":
  acol = addcol(acol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
  bcol = addcol(bcol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "sub":
  acol = subcol(acol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
  bcol = subcol(bcol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "xor":
  acol = xorcol(acol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
  bcol = xorcol(bcol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "bnw":
  acol = bnwcol(acol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
  bcol = bnwcol(bcol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "sep":
  acol = sepcol(acol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
  bcol = sepcol(bcol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "rmp":
  acol = rmpcol(acol,sys.argv[2],sys.argv[3],int(sys.argv[4]))
  bcol = rmpcol(bcol,sys.argv[2],sys.argv[3],int(sys.argv[4]))
 if sys.argv[1] == "rnd":
  acol = rndcol(acol,sys.argv[2],int(sys.argv[3]))
  bcol = rndcol(bcol,sys.argv[2],int(sys.argv[3]))
 if sys.argv[1] == "pow":
  acol = powcol(acol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
  bcol = powcol(bcol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "exp":
  acol = expcol(acol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
  bcol = expcol(bcol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "map":
  acol = mapcol(acol,sys.argv[2:])
  bcol = mapcol(bcol,sys.argv[2:])
 if sys.argv[1] == "uni":
  acol = unicol(acol,sys.argv[2])
  bcol = unicol(bcol,sys.argv[2])
 if sys.argv[1] == "col":
  acol = colcol(acol,sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
  bcol = colcol(bcol,sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
 if sys.argv[1] == "pos":
  acol = poscol(acol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
  bcol = poscol(bcol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "emp":
  acol = empcol(acol,sys.argv[2:])
  bcol = empcol(bcol,sys.argv[2:])
 if sys.argv[1] == "dmp":
  acol = dmpcol(acol,sys.argv[2:])
  bcol = dmpcol(bcol,sys.argv[2:])
 if sys.argv[1] == "gam":
  acol = gamcol(acol,float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))
  bcol = gamcol(bcol,float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))
 if sys.argv[1] == "shu":
  acol = shucol(acol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]))
  bcol = shucol(bcol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]))
 if sys.argv[1] == "old":
  acol = oldcol(acol,int(sys.argv[2]),int(sys.argv[3]))
  bcol = oldcol(bcol,int(sys.argv[2]),int(sys.argv[3]))
 if sys.argv[1] == "dep":
  acol = depcol(acol,sys.argv[2],sys.argv[3])
  bcol = depcol(bcol,sys.argv[2],sys.argv[3])
 if sys.argv[1] == "ppr":
  acol = pprcol(acol,sys.argv[2])
  bcol = pprcol(bcol,sys.argv[2])
 if sys.argv[1] == "ipr":
  acol = iprcol(acol,sys.argv[2],sys.argv[3])
  bcol = iprcol(bcol,sys.argv[2],sys.argv[3])
 if sys.argv[1] == "int":
  acol = intcol(acol,float(sys.argv[2]),sys.argv[3],sys.argv[4],sys.argv[5])
  bcol = intcol(bcol,float(sys.argv[2]),sys.argv[3],sys.argv[4],sys.argv[5])
 if sys.argv[1] == "fun":
  acol = funcol(acol,sys.argv[2],sys.argv[3],sys.argv[4])
  bcol = funcol(bcol,sys.argv[2],sys.argv[3],sys.argv[4])
 if sys.argv[1] == "lum":
  acol = lumcol(acol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]))
  bcol = lumcol(bcol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]))
 if sys.argv[1] == "dpr":
  acol = dprcol(acol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
  bcol = dprcol(bcol,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
 if sys.argv[1] == "tht":
  acol = thtcol(acol,float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))
  bcol = thtcol(bcol,float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))
 sys.stdout.write(chr(int(acol[0:2],16)))
 sys.stdout.write(chr(int(bcol[0:2],16)))
 sys.stdout.write(chr(int(acol[2:4],16)))
 sys.stdout.write(chr(int(bcol[2:4],16)))
 sys.stdout.write(chr(int(acol[4:6],16)))
 sys.stdout.write(chr(int(bcol[4:6],16)))
 sys.stdout.write(o[6])
 sys.stdout.write(o[7])
 n = n-1
 if not o:
  break
