import sys
mode = sys.argv[1]
after = int(sys.argv[5])
dose=float(sys.argv[6])
i = 0
while after:
 i = (int(sys.argv[2])*i+int(sys.argv[3])) % int(sys.argv[4])
 after=after-1

while True:
 o = sys.stdin.read(2)
 i = (int(sys.argv[2])*i+int(sys.argv[3])) % int(sys.argv[4])
 r = ord(o[1])*256 + ord(o[0])
 if mode == "enc":
  r = int((((r + i) % 65536)*dose)+(r*(1-dose)))
 if mode == "dec":
  r = int((((r - i) % 65536)*dose)+(r*(1-dose)))
 sys.stdout.write("%s%s" %(chr(r % 256),chr(r / 256)))