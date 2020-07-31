import sys
m = 0
def rgb2yuv(color):
 yuv = [0] * 3
 yuv[0] = color[0] *  .299000 + color[1] *  .587000 + color[2] *  .114000
 yuv[1] = color[0] * -.168736 + color[1] * -.331264 + color[2] *  .500000 + 128;
 yuv[2] = color[0] *  .500000 + color[1] * -.418688 + color[2] * -.081312 + 128;
 return yuv

while True:
 o = sys.stdin.read(3)
 final = rgb2yuv([ord(o[0]),ord(o[1]),ord(o[2])])
 q = final[0]
 if bool((m/int(sys.argv[1])) % 2):
  p = final[1]
 else:
  p = final[2]
 sys.stdout.write(chr(int(p/2)))
 sys.stdout.write(chr((int(q/2)+128)))
 m = m + 1