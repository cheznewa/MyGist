import sys
after = int(sys.argv[4])
i = 0
while after:
 i = (int(sys.argv[1])*i+int(sys.argv[2])) % int(sys.argv[3])
 after=after-1

while True:
 o = sys.stdin.read(2)
 i = (int(sys.argv[1])*i+int(sys.argv[2])) % int(sys.argv[3])
 r = ord(o[1])*256 + ord(o[0])
 r = r ^ (65535*(i%2))
 sys.stdout.write("%s%s" %(chr(r % 256),chr(r / 256)))