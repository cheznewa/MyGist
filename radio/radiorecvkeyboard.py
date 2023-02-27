import sys
from struct import unpack
import keyboard
min = int(sys.argv[1])
max = int(sys.argv[2])
inc = int(sys.argv[4])
u=0
while True:
 o = sys.stdin.read(4)
 n = unpack("I",o)[0]
 if (n >= min) and (n < max):
  if sys.argv[3] == "16":
   a = int((65536.0*(n-min)/(float(max)-float(min))))
   p = int(a % 256)
   q = int(a / 256)
   sys.stdout.write("%s%s" %(chr(p),chr(q)))
  if sys.argv[3] == "8":
   i = int((256.0*(n-min)/(float(max)-float(min))))
   sys.stdout.write("%s" %(chr(i)))
 if n == max-1:
  sys.stderr.write("\x07")
 if u == 0:
  if keyboard.is_pressed("left"):
   min = min - inc
   max = max - inc
   sys.stderr.write("\nRange Current :: %s-%s\n" %(min,max))
  if keyboard.is_pressed("right"):
   min = min + inc
   max = max + inc
   sys.stderr.write("\nRange Current :: %s-%s\n" %(min,max))
 u = (u+1)%30000