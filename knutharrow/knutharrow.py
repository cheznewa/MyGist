import sys
a = int(sys.argv[1])
b = int(sys.argv[3])
z = int(sys.argv[2])
m = sys.argv[4]
if m[-1:] == "b":
 m = pow(2,int(m[:-1]))-1
x = a
for l in range(z-1):
 for n in range(b-1):
  x = pow(a,x,int(m))
 a = x

sys.stdout.write("%s\n" %(a))