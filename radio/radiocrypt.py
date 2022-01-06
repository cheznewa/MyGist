import sys
mode = sys.argv[1]
a = 0
while True:
 o = sys.stdin.read(2)
 a = (int(sys.argv[2])*a+int(sys.argv[3])) % int(sys.argv[4])
 i = a % 333333
 r = ord(o[1])*256 + ord(o[0])
 if mode == "enc":
  r = (r + i) % 65536
 if mode == "dec":
  r = (r - i) % 65536
 sys.stdout.write("%s%s" %(chr(r % 256),chr(r / 256)))