import sys
import re
price=0
for o in sys.stdin:
 if re.search("<TTGlyph ",o):
  price=price/1.1
 if re.search("<pt ",o):
  if re.search(" on=\"0\"",o):
   price=price+0.2
  else:
   price=price+0.1
sys.stdout.write("%s\n" %(price))