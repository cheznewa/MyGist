import sys
if not "farbfeld" == sys.stdin.read(8):
 exit(1)
size = sys.stdin.read(8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
n = x*y
while bool(n):
 o = sys.stdin.read(8)
 r = ord(o[0])
 g = ord(o[2])
 b = ord(o[4])
 a = ord(o[6])
 r = int(r*(a/255.0))
 g = int(g*(a/255.0))
 b = int(b*(a/255.0))
 sys.stdout.write("\x1b[38;2;%s;%s;%sm%s%s" %(r,g,b,unichr(0x2588),unichr(0x2588)))
 n=n-1
 if not bool(n%x):
  sys.stdout.write("\n")

sys.stdout.write("\x1b[0m")