import sys
fs = [0] * (len(sys.argv)-1)
for fsi in range(len(sys.argv)-1):
 fs[fsi] = open(sys.argv[fsi+1],"r")

while True:
 for h in range(len(sys.argv)-1):
  ff = fs[h].read(4)
  sys.stdout.write(ff)
 if not ff:
  break