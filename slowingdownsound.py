import sys
rate = int(sys.argv[1])
byte = int(sys.argv[2])
slow = float(sys.argv[3])
leng = float(sys.argv[4])
n = 0
l = 1.0
while True:
 if l>(l*n)%1:
  o = sys.stdin.read(byte)
 if n >= leng*rate:
  l = l-(1/(float(slow)*float(rate)))
 sys.stdout.write(o)
 n = n+1
 if n > (leng+slow)*rate:
  break