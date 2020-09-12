import sys
m = 0
def rgb2yuv(color):
 yuv = [0] * 3
 yuv[0] = color[0] *  .299000 + color[1] *  .587000 + color[2] *  .114000
 yuv[1] = color[0] * -.168736 + color[1] * -.331264 + color[2] *  .500000 + 128;
 yuv[2] = color[0] *  .500000 + color[1] * -.418688 + color[2] * -.081312 + 128;
 return yuv

q = 0
while True:
 o = sys.stdin.read(3)
 final = rgb2yuv([ord(o[0]),ord(o[1]),ord(o[2])])
 if bool(m % 2):
  q = sys.stdout.write(chr((int(final[0]/2)+128)))
 else:
  if bool((m/int(sys.argv[1])) % 2):
   sys.stdout.write(chr(int(final[1]/4)))
  else:
   sys.stdout.write(chr(int(final[2]/4)+64))
 m = m + 1