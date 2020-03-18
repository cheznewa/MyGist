import sys
import os
pointsize = float(sys.argv[1])
bg = sys.argv[2]
fg = sys.argv[3]
strokewidth = int(sys.argv[4])
output = sys.argv[5]
base = pointsize/2
vecx=[[0,1],[0.0,0.5,1],[0,0,0.5,0.5,1,1],[0,0,1,1],[0.5,0.5],[0,0,0.5,0.5,1,1],[0.0,0.5,1],[0,0,1,1]]
vecy=[[0.5,0.5],[1,0,1],[0,1,1,0,1,1,0.0],[0,1,0,1],[0,1],    [1,0,0,1,0,0,1]  ,[0,1,0],[1,0,1,0]]
while True:
 o = sys.stdin.read(2)
 z = (ord(o[1])*256)+ord(o[0])
 a = (z/pow(len(vecx),4))%len(vecx)
 b = (z/pow(len(vecx),3))%len(vecx)
 c = (z/pow(len(vecx),2))%len(vecx)
 d = (z/pow(len(vecx),1))%len(vecx)
 drawa = drawb = drawc = drawd = ""
 for f in range(len(vecx[a])):
  x = float(vecx[a][f])*base
  y = float(vecy[a][f])*base
  drawa += " %s,%s " %(x,y)
 for f in range(len(vecx[b])):
  x = (float(vecx[b][f])*base)+base+2
  y = float(vecy[b][f])*base
  drawb += " %s,%s " %(x,y)
 for f in range(len(vecx[c])):
  x = float(vecx[c][f])*base
  y = (float(vecy[c][f])*base)+base+2
  drawc += " %s,%s " %(x,y)
 for f in range(len(vecx[d])):
  x = (float(vecx[d][f])*base)+base+2
  y = (float(vecy[d][f])*base)+base+2
  drawd += " %s,%s " %(x,y)
 os.system("convert -size %sx%s xc:%s -fill none -stroke %s -strokewidth %s -draw 'polyline %s polyline %s polyline %s polyline %s' tmp.png" %(pointsize+8,pointsize+4,bg,fg,strokewidth,drawa,drawb,drawc,drawd))
 if os.path.isfile(output):
  os.system("convert +append %s tmp.png %s" %(output,output))
 else:
  os.system("convert tmp.png %s" %(output))
