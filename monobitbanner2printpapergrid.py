import sys
import time
s = 0
sys.stdout.write("NEG = None\nPOS = Cross\nRET = New Line\n")
while True:
 s = s + 1
 i = sys.stdin.read(1)
 if i == "\x2e":
  sys.stdout.write("NEG")
 elif i == "\x40":
  sys.stdout.write("POS")
 elif i == "\x0a":
  sys.stdout.write("RET")
 else:
  exit(1)
 sys.stdout.write(" - %s" %(s))
 time.sleep(float(sys.argv[1]))
 sys.stdout.write("\n")
 if not i:
  break
