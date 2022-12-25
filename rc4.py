import sys
i=0
j=0
S=map(int,sys.argv[1:257])
while True:
 z=sys.stdin.read(1)
 if not z:
  break
 i=(i+1)%256
 j=(j+S[i])%256
 a=S[i]
 b=S[j]
 S[i]=b
 S[j]=a
 c=S[(S[i]+S[j])%256]
 sys.stdout.write(chr(ord(z)^c))