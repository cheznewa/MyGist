import sys
from base58 import b58encode_int
min = int(sys.argv[1])
max = int(sys.argv[2])
while True:
 o = sys.stdin.read(1)
 c = str(format(ord(o),"08b"))
 for d in range(8):
  if bool(int(c[d])):
   sys.stdout.write(b58encode_int(max-1))
  else:
   sys.stdout.write(b58encode_int(min))
  sys.stdout.write("\n")