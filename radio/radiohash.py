import sys
from base58 import b58decode_int
min = int(sys.argv[1])
max = int(sys.argv[2])
j = max - min
hash = [0] * j
for o in sys.stdin:
 if int(b58decode_int(o)) >= min and int(b58decode_int(o)) < max:
  i = b58decode_int(o)-min
  hash[i] = (hash[i] + 1) % 10

for u in range(j):
 sys.stdout.write("%s" %(hash[u]))
sys.stdout.write("\n")