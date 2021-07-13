import sys
if not "farbfeld" == sys.stdin.read(8):
 sys.stdout.write("Accept Only Farbfeld Format")
 exit(1)

size = sys.stdin.read(8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
w = x*y
n = 0
l = 0
m = [0] * (x*2)
sys.stdout.write("farbfeld")
sys.stdout.write(size)
while w > n:
 o = sys.stdin.read(8)
 m[l] = ord(o[0])
 l = l+1
 if not (x*2) > l:
  p = [0] * (4*x)
  for h in range(x/2):
   r = m[(h*2)]
   g = m[(h*2)+1]
   gg= m[(h*2)+x]
   b = m[(h*2)+x+1]
   p[h*3] = r
   p[(h*3)+1] = (g+gg)/2
   p[(h*3)+2] = b
  for i in range(x/2):
   sys.stdout.write(chr(p[i*3]))
   sys.stdout.write(chr(p[i*3]))
   sys.stdout.write(chr(p[(i*3)+1]))
   sys.stdout.write(chr(p[(i*3)+1]))
   sys.stdout.write(chr(p[(i*3)+2]))
   sys.stdout.write(chr(p[(i*3)+2]))
   sys.stdout.write(o[6])
   sys.stdout.write(o[7])
   sys.stdout.write(chr(p[i*3]))
   sys.stdout.write(chr(p[i*3]))
   sys.stdout.write(chr(p[(i*3)+1]))
   sys.stdout.write(chr(p[(i*3)+1]))
   sys.stdout.write(chr(p[(i*3)+2]))
   sys.stdout.write(chr(p[(i*3)+2]))
   sys.stdout.write(o[6])
   sys.stdout.write(o[7])
  for i in range(x/2):
   sys.stdout.write(chr(p[i*3]))
   sys.stdout.write(chr(p[i*3]))
   sys.stdout.write(chr(p[(i*3)+1]))
   sys.stdout.write(chr(p[(i*3)+1]))
   sys.stdout.write(chr(p[(i*3)+2]))
   sys.stdout.write(chr(p[(i*3)+2]))
   sys.stdout.write(o[6])
   sys.stdout.write(o[7])
   sys.stdout.write(chr(p[i*3]))
   sys.stdout.write(chr(p[i*3]))
   sys.stdout.write(chr(p[(i*3)+1]))
   sys.stdout.write(chr(p[(i*3)+1]))
   sys.stdout.write(chr(p[(i*3)+2]))
   sys.stdout.write(chr(p[(i*3)+2]))
   sys.stdout.write(o[6])
   sys.stdout.write(o[7])
  m = [0] * (x*2)
  n = n+(x*2)
  l = 0