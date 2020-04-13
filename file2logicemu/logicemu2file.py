import sys
import re
for o in sys.stdin.readlines():
 if re.search("B",o) or re.search("b",o):
  b = o[2:10]
  b = re.sub("b","0",b)
  b = re.sub("B","1",b)
  b = int(b,2)
  sys.stdout.write(chr(b))