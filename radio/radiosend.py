import sys
min = int(sys.argv[1])
max = int(sys.argv[2])
while True:
 o = sys.stdin.read(1)
 sys.stdout.write("%s\n" %(int((ord(o)/256.0)*(max-min))+min))