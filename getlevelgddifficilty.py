m = (918, 1327, 1328, 1584)
f = (920, 923, 924, 921)
s = (1705, 740, 1619, 1706, 741, 742, 1620, 184, 1707, 1734, 678, 185, 1708, 1736, 187, 679, 1709, 1710, 186, 1735, 188, 680, 183)
p = (8, 218, 458, 39, 103, 144, 392, 205, 216, 145, 217, 459, 177, 178, 179)
c = (1, 83, 2, 3, 4, 5, 502, 6, 7, 1743, 1744, 681, 682)
d = 0
pa = 0
pb = 0
import sys
o = sys.stdin.read()
while True:
  pa = o.find(";1,",pa)
  pb = o.find(",",pa+3)
  if pa == -1:
   break
  n = int(o[pa+3:pb])
  if n in c:
   d = d + 1
  if n in p:
   d = d + 10
  if n in s:
   d = d + 1000
  if n in f:
   d = d + 10
  if n in m:
   d = d + 100
  else:
   d = d - 1
  pa = pb + len(str(n))

sys.stdout.write("%s\n" %(d))