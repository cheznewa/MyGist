import sys
import re
price=0
st=False
for o in sys.stdin:
 if re.search("<TTGlyph ",o):
  price=price/1.1
 if re.search("<pt ",o):
  if re.search(" on=\"0\"",o):
   price=price+0.2
  if re.search(" on=\"1\"",o):
   price=price+0.1
 if re.search("<CharString ",o):
  st = True
  price=price/1.1
 if re.search("moveto",o) and st:
  price=price+1
 if re.search("lineto",o) and st:
  price=price+3
 if re.search("curveto",o) and st:
  price=price+6
 if re.search("endchar",o) and st:
  st = False

sys.stdout.write("%s\n" %(price))