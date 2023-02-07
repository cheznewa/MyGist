import sys

rate = int(sys.argv[1])
pase = float(sys.argv[2])
leng = float(sys.argv[3])

l=0
n=0
m=0

while True:
 if n >= pase*rate:
  m=m+1
 l=min(float(m)/(leng*rate),1)
 o = sys.stdin.read(2)
 r = ord(o[1])*256 + ord(o[0])
 i = n%2
 r = int(((r ^ (65535*i))*l)+(r*(1-l)))
 sys.stdout.write("%s%s" %(chr(r % 256),chr(r / 256)))
 n=n+1