import sys
from base58 import b58decode_int
min = int(sys.argv[1])
max = int(sys.argv[2])
len = int(sys.argv[3])
hash = [0] * len
while True:
 o = sys.stdin.read(4)
 n = unpack("I",o)[0]
 if n) >= min and n < max:
  i = int((len*(n-min)/(float(max)-float(min))))
  hash[i] = (hash[i] + 1) % 10

for u in range(len):
 sys.stdout.write("%s" %(hash[u]))
sys.stdout.write("\n")