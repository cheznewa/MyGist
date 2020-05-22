import sys
import os
n = 0
rate = int(sys.argv[1])
size = sys.argv[2]
fps = int(sys.argv[3])
siza = size.split("x")
length = (fps*(int(siza[0])*int(siza[1])))/rate
old = audio = 0
while True:
 o = sys.stdin.read(2)
 audio = audio + ord(o[0])
 video = o[1]
 os.write(7,video)
 if n >= length:
  n = 0
 if n == 0:
  os.write(4,chr(audio/length))
  audio = 0
 n = n + 1