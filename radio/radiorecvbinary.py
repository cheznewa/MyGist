import sys
from base58 import b58decode_int
min = int(sys.argv[1])
max = int(sys.argv[2])
n = 1
c = ""
b = [0] * 8
for o in sys.stdin:
 if int(b58decode_int(o)) == min:
  b[n-1] = 0
 if int(b58decode_int(o)) == (max-1):
  b[n-1] = 1
 if n == 8:
  for v in range(8):
   c = c + str(b[v])
  sys.stdout.write(chr(int(c,2)))
  n = 0
  c = ""
 n = n + 1