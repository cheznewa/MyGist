import sys
n = 0
i = 0
yy = 128
uu = 128
vv = 128
def yuv2rgb(color):
 rgb = [0] * 3
 rgb[0] = color[0] + 1.4075 * (color[2] - 128)
 rgb[1] = color[0] - 0.3455 * (color[1] - 128) - (0.7169 * (color[2] - 128))
 rgb[2] = color[0] + 1.7790 * (color[1] - 128)
 return rgb

while True:
 o = ord(sys.stdin.read(1))
 if o <= 127:
  if bool((n/int(sys.argv[1])) % 2):
   if o < 64:
    uu = o*4
   else:
    uu = 127
  else:
   if o >= 64:
    vv = (o-64)*4
   else:
    vv = 127
 if o > 127:
  yy = (o-128)*2
 final = yuv2rgb([yy,uu,vv])
 if final[0] >= 255:
  final[0] = 255
 if final[0] <= 0:
  final[0] = 0
 if final[1] >= 255:
  final[1] = 255
 if final[1] <= 0:
  final[1] = 0
 if final[2] >= 255:
  final[2] = 255
 if final[2] <= 0:
  final[2] = 0
 sys.stdout.write("%s%s%s" %(chr(int(final[0])),chr(int(final[1])),chr(int(final[2]))))
 n = n + 1