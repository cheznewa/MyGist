import sys
import random
import os
webname = str(sys.argv[1])
npages = int(sys.argv[2])
syllab = "azertyuiopqsdfghjklmwxcvbn3"
random.seed(webname)
syc = len(syllab)
for l in range(1,npages+1):
 fs = open("%s.txt" %(l),"w")
 words = ""
 links = []
 for m in range(random.randint(500,5000)):
  if random.randint(1,200) == 100:
   links.append(random.randint(1,npages))
  else:
   for n in range(random.randint(2,10)):
    words += syllab[random.randint(0,syc-1)]
  words += " "
 fs.write(words)
 fs.close()
 links = sorted(links)
 for t in links:
  sys.stdout.write("%s\t%s\r\n" %(l,t))