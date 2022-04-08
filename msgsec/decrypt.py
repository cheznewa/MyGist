import sys
import os
n=int(sys.stdin.read())
u=""
while True:
 h=os.read(9,1)
 u=u+h
 if not h:
  break
n=n%int(u)
msg=""
while n:
 n,o=divmod(n,256)
 msg=chr(o)+msg
sys.stdout.write("%s" %(msg))