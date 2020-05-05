import sys
a = int(sys.argv[1])
b = int(sys.argv[3])
z = int(sys.argv[2])
m = int(sys.argv[4])
x = a
for l in range(z):
 for n in range(b):
  x = pow(a,x,m)
 a = x

sys.stdout.write("%s\n" %(a))