import sys
import re
price = 0
v = True
while True:
 o = sys.stdin.read(1)
 if "\"" == o:
  v = not(v)
 if v:
  if (o == "<") or (o == ">") or (o == "v") or (o == "^"):
   price=price+3
  elif (o == "[") or (o == "]") or (o == "w") or (o == "m"):
   price=price+5
  elif o == "i":
   price=price+10
  elif o == "I":
   price=price+100
  elif o == " ":
   price=price/1.1
  else:
   price=price+1
 if not o:
  break

sys.stdout.write("%s\n" %(price))