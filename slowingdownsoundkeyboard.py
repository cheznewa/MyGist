import sys
import keyboard
rate = int(sys.argv[1])
byte = int(sys.argv[2])
slow = float(sys.argv[3])
n = 0
l = 1.0
u = 0
a = False
while True:
 if l>(l*n)%1:
  o = sys.stdin.read(byte)
 if a:
  l = l-(1/(float(slow)*float(rate)))
  if n > m+(rate*slow):
   break
 sys.stdout.write(o)
 if u == 0:
  if keyboard.is_pressed("down"):
   a = True
   m = n
 n = n+1
 u = (u+1)%10000