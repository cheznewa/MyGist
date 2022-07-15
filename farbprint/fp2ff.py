import sys
if not "farbprit" == sys.stdin.read(8):
 exit(1)
size = sys.stdin.read(8)
x = (pow(256,3)*ord(size[0]))+(pow(256,2)*ord(size[1]))+(pow(256,1)*ord(size[2]))+(pow(256,0)*ord(size[3]))
y = (pow(256,3)*ord(size[4]))+(pow(256,2)*ord(size[5]))+(pow(256,1)*ord(size[6]))+(pow(256,0)*ord(size[7]))
n = x*y
sys.stdout.write("farbfeld")
sys.stdout.write(size)
while bool(n):
 o = sys.stdin.read(8)
 c = (ord(o[0])*256)+ord(o[1])
 m = (ord(o[2])*256)+ord(o[3])
 y = (ord(o[4])*256)+ord(o[5])
 k = (ord(o[6])*256)+ord(o[7])
 # Source From ::::::: https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
 r = (1-(c/65535.0))*(1-(k/65535.0))
 g = (1-(m/65535.0))*(1-(k/65535.0))
 b = (1-(y/65535.0))*(1-(k/65535.0))
 # End Source
 sys.stdout.write("%s%s%s%s%s%s%s%s" %(chr(int(r*65535)/256),chr(int(r*65535)%256),chr(int(g*65535)/256),chr(int(g*65535)%256),chr(int(b*65535)/256),chr(int(b*65535)%256),chr(255),chr(255)))
 n=n-1