import sys
if not "farbfeld" == sys.stdin.read(8):
 sys.stdout.write("Accept Only Farbfeld Format.\n")
 exit(1)

size = sys.stdin.read(8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
w = x*y
n = 0
sys.stdout.write("farbfeld")
sys.stdout.write(size)
while w > n:
 o = sys.stdin.read(8)
 if bool((n/x)%2):
  if bool(n%2):
   r = o[4]
  else:
   r = o[2]
 else:
  if bool(n%2):
   r = o[2]
  else:
   r = o[0]
 sys.stdout.write("%s%s%s%s%s%s%s%s" %(r,r,r,r,r,r,o[6],o[7]))
 n = n+1