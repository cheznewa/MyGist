import sys
import re
fs = open(sys.argv[1],"rb")
for o in sys.stdin.read():
 if o == "?":
  if bool(ord(fs.read(1))%2):
   sys.stdout.write("F")
  else:
   sys.stdout.write("f")
 else:
  sys.stdout.write(o)