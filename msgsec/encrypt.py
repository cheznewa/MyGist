import sys
import random
import os
msg=0
o=sys.stdin.read()
for n in o:
 msg=msg*256+ord(n)

m=random.getrandbits(int(sys.argv[1]))

sys.stdout.write("%s" %(msg+random.getrandbits(int(sys.argv[1]))*m))
os.write(9,str(m))