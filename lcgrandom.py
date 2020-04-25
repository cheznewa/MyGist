import sys
while True:
 sys.stdout.write(chr(int(sys.argv[1]) % 256))
 sys.argv[1] = (int(sys.argv[2])*int(sys.argv[1])+int(sys.argv[3])) % int(sys.argv[4])