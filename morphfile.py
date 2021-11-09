import sys
afile = open(sys.argv[1],"r")
bfile = open(sys.argv[2],"r")
reglo = float(sys.argv[3])
while True:
 a = ord(afile.read(1))
 b = ord(bfile.read(1))
 h = b - a
 f = a + (h*reglo)
 sys.stdout.write(chr(int(f)))