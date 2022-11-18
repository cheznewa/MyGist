import sys

i=0

while True:
 o = sys.stdin.read(2)
 r = ord(o[1])*256 + ord(o[0])
 r = r ^ (65535*i)
 i = (i+1)%2
 sys.stdout.write("%s%s" %(chr(r % 256),chr(r / 256)))