import sys
import math
fs = open(sys.argv[1])
begin = int(sys.argv[2])
end = int(sys.argv[3])
lines = fs.readlines()
mux = int(lines[0])

def tri(n):
 return (n*(n+1))/2

for i in range(begin,end+1):
 a = 0.0
 e = []
 for j in range(mux):
  e.append((i*2) / math.factorial(j+1) % (j+1))
  a = a + float(lines[tri(j+1)+e[j]])
 sys.stdout.write(chr(int(a)%256))
