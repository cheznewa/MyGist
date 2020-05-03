# Télévision Render From TV's Phelÿn
import sys
r = 0
g = 0
b = 0
t = 0
flame = [250,170,30]
r = 256
while True:
 o = sys.stdin.read(3)
 t += abs(r - ord(o[0])) + abs(g - ord(o[1])) + abs(b - ord(o[2]))
 rr = (int((flame[0]*(t/1024.0) + ord(o[0]))))
 if rr >= 255:
  rr = 255
 if rr <= 0:
  rr = 0
 sys.stdout.write(chr(rr))
 rg = (int((flame[1]*(t/1024.0) + ord(o[1]))))
 if rg >= 255:
  rg = 255
 if rg <= 0:
  rg = 0
 sys.stdout.write(chr(rg))
 rb = (int((flame[2]*(t/1024.0) + ord(o[2]))))
 if rb >= 250:
  rb = 255
 if rb <= 0:
  rb = 0
 sys.stdout.write(chr(rb))
 if t >= 0:
  t = t - r
 r = ord(o[0])
 g = ord(o[1])
 b = ord(o[2])