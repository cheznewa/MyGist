import sys

dose=float(sys.argv[1])
i=0

while True:
 o = sys.stdin.read(2)
 r = ord(o[1])*256 + ord(o[0])
 r = r ^ (int(65535*dose)*i)
 i = (i+1)%2
 sys.stdout.write("%s%s" %(chr(r % 256),chr(r / 256)))