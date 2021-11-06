import sys
from struct import unpack
min = int(sys.argv[1])
max = int(sys.argv[2])
lng = int(sys.argv[3])
hash = [0] * lng
while True:
 o = sys.stdin.read(4)
 if not len(o) == 4:
  break
 n = unpack("I",o)[0]
 if (n >= min) and (n < max):
  i = int((lng*(n-min)/(float(max)-float(min))))
  hash[i] = (hash[i] + 1) % 10

for u in range(lng):
 sys.stdout.write("%s" %(hash[u]))
sys.stdout.write("\n")