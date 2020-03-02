import sys
fs = open(sys.argv[1])
lines = fs.readlines()
res = lines[0]
rex = res.split(" ")
a = []
for n in range(1,int(rex[1])+1):
 data = lines[n]
 spl = data.split(" ")
 a.append(spl)

for p in range(int(sys.argv[2]),int(sys.argv[3])):
 o = 0.0
 for q in range(int(rex[1])):
  o = o + float(a[q][p/(pow(int(rex[0]),q))%int(rex[0])])
 sys.stdout.write(chr(int(o)))