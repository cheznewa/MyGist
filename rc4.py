import sys
i=0
j=0
S=map(int,sys.argv[2:258])
while True:
 i=(i+1)%256
 j=(j+S[i])%256
 a=S[i]
 b=S[j]
 S[i]=b
 S[j]=a
 c=S[(S[i]+S[j])%256]
 if "crypto" == sys.argv[1]:
  z=sys.stdin.read(1)
  if not z:
   break
  sys.stdout.write(chr(ord(z)^c))
 elif "random" == sys.argv[1]:
  sys.stdout.write(chr(c))