import sys
from struct import unpack
min = int(sys.argv[1])
max = int(sys.argv[2])
n = 0
c = ""
b = [0] * 8
while True:
 o = sys.stdin.read(4)
 n = unpack("I",o)[0]
 if n == min+1:
  for v in range(8):
   c = c + str(b[v])
  sys.stdout.write(chr(int(c,2)))
  n = 0
  c = ""
 elif n == min:
  b[n] = 0
  n = n+1
 elif n == (max-1):
  b[n] = 1
  n = n+1