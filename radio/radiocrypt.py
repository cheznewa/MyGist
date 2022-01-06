import sys
mode = sys.argv[1]
i = 0
while True:
 o = sys.stdin.read(2)
 i = (int(sys.argv[2])*i+int(sys.argv[3])) % int(sys.argv[4])
 r = ord(o[1])*256 + ord(o[0])
 if mode == "enc":
  r = (r + i) % 65536
 if mode == "dec":
  r = (r - i) % 65536
 sys.stdout.write("%s%s" %(chr(r % 256),chr(r / 256)))