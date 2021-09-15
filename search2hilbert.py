import sys
from hilbertcurve.hilbertcurve import HilbertCurve # https://github.com/galtay/hilbertcurve/releases/tag/v1.0.2
hilbert = HilbertCurve(int(sys.argv[1]),2)
o = sys.stdin.read(pow(pow(2,int(sys.argv[1])),2))
p = 0
while True:
 p = o.find(sys.argv[2],p)
 c = hilbert.coordinates_from_distance(p)
 sys.stdout.write("<span style=\"position:absolute;left:%s;top:%s;\">X</span>\n" %(c[0],c[1]))
 p = p + len(sys.argv[2])