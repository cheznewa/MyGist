import sys

rate=int(sys.argv[1])
pase=float(sys.argv[2])
leng=float(sys.argv[3])
mode=sys.argv[4]

n=0

if mode == "u":
 l=0
 m=0
elif mode == "d":
 l=1
 m=leng*rate

while True:
 if n >= pase*rate:
  if mode == "u":
   m=m+1
  elif mode == "d":
   m=m-1
 l=max(min(float(m)/(leng*rate),1),0)
 o = sys.stdin.read(2)
 r = ord(o[1])*256 + ord(o[0])
 i = n%2
 r = int(((r ^ (65535*i))*l)+(r*(1-l)))
 sys.stdout.write("%s%s" %(chr(r % 256),chr(r / 256)))
 n=n+1