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

vgapal = ["000000","0000AA","00AA00","00AAAA","AA0000","AA00AA","AA5500","AAAAAA","555555","5555FF","55FF55","55FFFF","FF5555","FF55FF","FFFF55","FFFFFF","000000","101010","202020","353535","454545","555555","656565","757575","8A8A8A","9A9A9A","AAAAAA","BABABA","CACACA","DFDFDF","EFEFEF","FFFFFF","0000FF","4100FF","8200FF","BE00FF","FF00FF","FF00BE","FF0082","FF0041","FF0000","FF4100","FF8200","FFBE00","FFFF00","BEFF00","82FF00","41FF00","00FF00","00FF41","00FF82","00FFBE","00FFFF","00BEFF","0082FF","0041FF","8282FF","9E82FF","BE82FF","DF82FF","FF82FF","FF82DF","FF82BE","FF829E","FF8282","FF9E82","FFBE82","FFDF82","FFFF82","DFFF82","BEFF82","9EFF82","82FF82","82FF9E","82FFBE","82FFDF","82FFFF","82DFFF","82BEFF","829EFF","BABAFF","CABAFF","DFBAFF","EFBAFF","FFBAFF","FFBAEF","FFBADF","FFBACA","FFBABA","FFCABA","FFDFBA","FFEFBA","FFFFBA","EFFFBA","DFFFBA","CAFFBA","BAFFBA","BAFFCA","BAFFDF","BAFFEF","BAFFFF","BAEFFF","BADFFF","BACAFF","000071","1C0071","390071","550071","710071","710055","710039","71001C","710000","711C00","713900","715500","717100","557100","397100","1C7100","007100","00711C","007139","007155","007171","005571","003971","001C71","393971","453971","553971","613971","713971","713961","713955","713945","713939","714539","715539","716139","717139","617139","557139","457139","397139","397145","397155","397161","397171","396171","395571","394571","515171","595171","615171","695171","715171","715169","715161","715159","715151","715951","716151","716951","717151","697151","617151","597151","517151","517159","517161","517169","517171","516971","516171","515971","000041","100041","200041","310041","410041","410031","410020","410010","410000","411000","412000","413100","414100","314100","204100","104100","004100","004110","004120","004131","004141","003141","002041","001041","202041","282041","312041","392041","412041","412039","412031","412028","412020","412820","413120","413920","414120","394120","314120","284120","204120","204128","204131","204139","204141","203941","203141","202841","2D2D41","312D41","352D41","3D2D41","412D41","412D3D","412D35","412D31","412D2D","41312D","41352D","413D2D","41412D","3D412D","35412D","31412D","2D412D","2D4131","2D4135","2D413D","2D4141","2D3D41","2D3541","2D3141","000000","000000","000000","000000","000000","000000","000000","000000"] # Source ::::::: https://commons.wikimedia.org/w/index.php?title=User:Psychonaut/ipalette.sh

import sys
while True:
 o = sys.stdin.read(1)
 if not o:
  break
 col = vgapal[ord(o)]
 if sys.argv[1] == "add":
  col = addcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "sub":
  col = subcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "xor":
  col = xorcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "bnw":
  col = bnwcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "sep":
  col = sepcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "rmp":
  col = rmpcol(col,sys.argv[2],sys.argv[3],int(sys.argv[4]))
 if sys.argv[1] == "rnd":
  col = rndcol(col,sys.argv[2],int(sys.argv[3]))
 if sys.argv[1] == "pow":
  col = powcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "exp":
  col = expcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "map":
  col = mapcol(col,sys.argv[2:])
 if sys.argv[1] == "uni":
  col = unicol(col,sys.argv[2])
 if sys.argv[1] == "col":
  col = colcol(col,sys.argv[2],int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
 if sys.argv[1] == "pos":
  col = poscol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
 if sys.argv[1] == "emp":
  col = empcol(col,sys.argv[2:])
 if sys.argv[1] == "dmp":
  col = dmpcol(col,sys.argv[2:])
 if sys.argv[1] == "gam":
  col = gamcol(col,float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]))
 if sys.argv[1] == "shu":
  col = shucol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]))
 if sys.argv[1] == "old":
  col = oldcol(col,int(sys.argv[2]),int(sys.argv[3]))
 if sys.argv[1] == "dep":
  col = depcol(col,sys.argv[2],sys.argv[3])
 if sys.argv[1] == "ppr":
  col = pprcol(col,sys.argv[2])
 if sys.argv[1] == "ipr":
  col = iprcol(col,sys.argv[2],sys.argv[3])
 if sys.argv[1] == "int":
  col = intcol(col,float(sys.argv[2]),sys.argv[3],sys.argv[4],sys.argv[5])
 if sys.argv[1] == "fun":
  col = funcol(col,sys.argv[2],sys.argv[3],sys.argv[4])
 if sys.argv[1] == "lum":
  col = lumcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6]),float(sys.argv[7]))
 if sys.argv[1] == "dpr":
  col = dprcol(col,int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
 vr = int(col[0:2],16)
 vg = int(col[2:4],16)
 vb = int(col[4:6],16)
 z = []
 for com in vgapal:
  ar = int(com[0:2],16)
  ag = int(com[2:4],16)
  ab = int(com[4:6],16)
  z.append(max(abs(vr-ar)+abs(vg-ag)+abs(vb-ab),0))
 d = 10000
 rcol = "000000"
 for n in range(256):
  if z[n] < d:
   d = z[n]
   c = n
 sys.stdout.write("%s" %(chr(c)))
