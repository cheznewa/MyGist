import sys
import time
s = 0
y = 1
sys.stdout.write("NEG = None\nPOS = Cross\nRET = New Line\n")
while True:
 s = s + 1
 i = sys.stdin.read(1)
 if i == ".":
  sys.stdout.write("NEG")
 elif i == "@":
  sys.stdout.write("POS")
 elif i == "\n":
  sys.stdout.write("RET")
  s = 0
  y = y + 1
 else:
  exit(1)
 sys.stdout.write(" - %s,%s" %(s,y))
 time.sleep(float(sys.argv[1]))
 sys.stdout.write("\n")
 if not i:
  break
