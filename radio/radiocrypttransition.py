import sys
mode = sys.argv[1]
after = int(sys.argv[5])
rate=int(sys.argv[6])
pase=float(sys.argv[7])
leng=float(sys.argv[8])
modg=sys.argv[9]
i = 0
n = 0
while after:
 i = (int(sys.argv[2])*i+int(sys.argv[3])) % int(sys.argv[4])
 after=after-1

if modg == "u":
 l=0
 m=0
elif modg == "d":
 l=1
 m=leng*rate

while True:
 if n >= pase*rate:
  if modg == "u":
   m=m+1
  elif modg == "d":
   m=m-1
 l=max(min(float(m)/(leng*rate),1),0)
 o = sys.stdin.read(2)
 i = (int(sys.argv[2])*i+int(sys.argv[3])) % int(sys.argv[4])
 r = ord(o[1])*256 + ord(o[0])
 if mode == "enc":
  r = int((((r + i) % 65536)*l)+(r*(1-l)))
 if mode == "dec":
  r = int((((r - i) % 65536)*l)+(r*(1-l)))
 sys.stdout.write("%s%s" %(chr(r % 256),chr(r / 256)))
 n=n+1