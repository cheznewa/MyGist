import sys
from PIL import Image
img = Image.open(sys.argv[1])
imga = img.resize((16,16))
r = list(bytearray(imga.getdata(0)))
g = list(bytearray(imga.getdata(1)))
b = list(bytearray(imga.getdata(2)))
sys.stdout.write("   lll\n   ^^^\n   |||I\n")
for n in range(16*16):
 if n < 8:
  if int(r[n]) >= int(sys.argv[2]):
   sys.stdout.write("s->B")
  else:
   sys.stdout.write("s->b")
 else:
  if int(r[n]) >= int(sys.argv[2]):
   sys.stdout.write("   B")
  else:
   sys.stdout.write("   b")
 if int(g[n]) >= int(sys.argv[2]):
  sys.stdout.write("B")
 else:
  sys.stdout.write("b")
 if int(b[n]) >= int(sys.argv[2]):
  sys.stdout.write("B\n")
 else:
  sys.stdout.write("b\n")

sys.stdout.write("\n")

sys.stdout.write("7g->D###############<-r1\n")
sys.stdout.write("6g->################<-c\n")
sys.stdout.write("5g->################\n")
sys.stdout.write("4g->################\n")
sys.stdout.write("    ################\n")
sys.stdout.write("    ################\n")
sys.stdout.write("    ################\n")
sys.stdout.write("    ################\n")
sys.stdout.write("    ################\n")
sys.stdout.write("    ################\n")
sys.stdout.write("    ################\n")
sys.stdout.write("    ################\n")
sys.stdout.write("    ################\n")
sys.stdout.write("    ################<-g08\n")
sys.stdout.write("    ################<-g09\n")
sys.stdout.write("    ################<-g10\n")
sys.stdout.write("    ^^^^\n")
sys.stdout.write("    ||||\n")
sys.stdout.write("    gggg\n")
sys.stdout.write("    3210\n")

sys.stdout.write("\n")

sys.stdout.write("1r-]c]c]c]c]c]c]c]c->l\n")
sys.stdout.write("    | | | | | | | |\n")
sys.stdout.write("    g g g g g g g g\n")
sys.stdout.write("    0 1 2 3 4 5 6 7\n")
sys.stdout.write("\n")
sys.stdout.write("   001\n   890\n   ggg\n   |||\n7g>#i#\n6g>###\n5g>###\n4g>###\n3g>###\n2g>###\n1g>###\n0g>###\n")
