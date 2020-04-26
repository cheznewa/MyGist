import sys
a = 0
while True:
 a = (int(sys.argv[1])*a+int(sys.argv[2])) % int(sys.argv[3])
 sys.stdout.write(chr(a % 256))