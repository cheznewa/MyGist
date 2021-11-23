import sys
import re
l = True
c = 0
for o in sys.stdin:
 if re.search("^DE,",o) and l:
  l = False
  c = c + 1
  fs = open("%s_%s.tti" %(c,o.split(",")[1]),"w")
  fs.write("OL,0,%s - %s\n" %(sys.argv[1],o.split(",")[1].rstrip('\n')))
 if re.search("^PN,",o) and l:
  l = False
  c = c + 1
  fs = open("%s_%s.tti" %(c,o.split(",")[1]),"w")
  fs.write("OL,0,%s - %s/%s\n" %(sys.argv[1],o[3:6],o[6:8]))
 if re.search("^OL,",o):
  l = True
 fs.write(o)