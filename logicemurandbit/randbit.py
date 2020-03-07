import sys
import re
import os
# randbit.py < circuit 3< randomsource
for o in sys.stdin.read():
 if o == "?":
  if bool(ord(os.read(3,1))%2):
   sys.stdout.write("F")
  else:
   sys.stdout.write("f")
 else:
  sys.stdout.write(o)