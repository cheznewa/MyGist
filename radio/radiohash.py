import sys
from base58 import b58decode_int
min = int(sys.argv[1])
max = int(sys.argv[2])
len = int(sys.argv[3])
hash = [0] * len
for o in sys.stdin:
 if int(b58decode_int(o)) >= min and int(b58decode_int(o)) < max:
  i = int((len*(int(b58decode_int(o))-min)/(float(max)-float(min))))
  hash[i] = (hash[i] + 1) % 10

for u in range(len):
 sys.stdout.write("%s" %(hash[u]))
sys.stdout.write("\n")