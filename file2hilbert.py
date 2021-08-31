import sys
from hilbertcurve.hilbertcurve import HilbertCurve # https://github.com/galtay/hilbertcurve/releases/tag/v1.0.2
hilbert = HilbertCurve(int(sys.argv[1]),2)
o = sys.stdin.read(pow(pow(2,int(sys.argv[1])),2))
a = format(pow(2,int(sys.argv[1])),"08x")
b = chr(int(a[0:2],16)) + chr(int(a[2:4],16)) + chr(int(a[4:6],16)) + chr(int(a[6:8],16))
sys.stdout.write("farbfeld%s%s" %(b,b))
for n in range(pow(pow(2,int(sys.argv[1])),2)):
 p = hilbert.distance_from_coordinates([n%pow(2,int(sys.argv[1])),n/pow(2,int(sys.argv[1]))])
 c = o[p]
 sys.stdout.write("%s%s%s%s%s%s%s%s" %(c,c,c,c,c,c,c,c))