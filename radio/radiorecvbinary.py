import sys
from base58 import b58decode_int
min = int(sys.argv[1])
max = int(sys.argv[2])
n = 0
c = ""
b = [0] * 8
for o in sys.stdin:
 if b58decode_int(o) == min+1:
  for v in range(8):
   c = c + str(b[v])
  sys.stdout.write(chr(int(c,2)))
  n = 0
  c = ""
 elif b58decode_int(o) == min:
  b[n] = 0
  n = n+1
 elif b58decode_int(o) == (max-1):
  b[n] = 1
  n = n+1