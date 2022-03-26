import sys
rate = int(sys.argv[1])
leng = float(sys.argv[2])
slow = float(sys.argv[3])
byte = int(sys.argv[4])
n = 0
l = 1.0
while True:
 if l>(l*n)%1:
  a = sys.stdin.read(byte)
 if n >= leng*rate:
  l = l-(1/(float(slow)*float(rate)))
 sys.stdout.write(a)
 n = n+1
 if n > (leng+slow)*rate:
  break