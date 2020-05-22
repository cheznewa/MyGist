import sys
import os
n = 0
rate = int(sys.argv[1])
size = sys.argv[2]
fps = int(sys.argv[3])
siza = size.split("x")
length = (fps*(int(siza[0])*int(siza[1])))/rate
while True:
 if n >= length:
  n = 0
 if n == 0:
  audio = ord(os.read(4,1))
 video = os.read(7,1)
 sys.stdout.write(chr(audio))
 sys.stdout.write(video)
 n = n + 1