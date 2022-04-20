import sys
fs = open(sys.argv[1],"r")
t = fs.read().split("\n")
h = 0
n = 0
while True:
 o = sys.stdin.read(1)
 if not o:
  break
 h = (h + int(t[ord(o)]) + n) % (pow(2,1024)-1)
 n = n+1

sys.stdout.write("%s\n" %(format(h,"0256x")))
