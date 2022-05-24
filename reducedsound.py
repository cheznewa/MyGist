import sys
byte = int(sys.argv[1])
qlty = float(sys.argv[2])
n = 0
while True:
 o = sys.stdin.read(byte)
 if qlty>(qlty*n)%1:
  oo = o
  sys.stdout.write(o)
 else:
  sys.stdout.write(oo)
 if not o:
  break
 n=n+1