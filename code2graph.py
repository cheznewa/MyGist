import sys
import re
for o in sys.stdin:
 a = ""
 b = ""
 t = False
 f = False
 g = True

 for x in o:
  if t:
   if bool(re.match("[a-zA-Z0-9_\[\]]",x)):
    b = b + x
    f = True
   else:
    if f:
     sys.stdout.write("%s %s\n" %(a,b))
    f = False
    b = ""
  else:
   if bool(re.match("[a-zA-Z0-9_\[\]]",x)):
    a = a + x
   elif x == "=":
    t = True