import sys
from PIL import Image
img = Image.open(sys.argv[1])
imga = img.resize((32,32))
r = list(bytearray(imga.getdata(0)))
g = list(bytearray(imga.getdata(1)))
b = list(bytearray(imga.getdata(2)))
sys.stdout.write("10g->D###############################<--g11\n")
sys.stdout.write("09g->################################<-f\n")
sys.stdout.write("08g->################################\n")
sys.stdout.write("07g->################################\n")
sys.stdout.write("06g->################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################<-g$\n")
sys.stdout.write("     ################################<-g$\n")
sys.stdout.write("     ################################<-g$\n")
sys.stdout.write("     ################################<-g$\n")
sys.stdout.write("     ################################<-g$\n")
sys.stdout.write("     ################################<-g$\n")
sys.stdout.write("     ################################<-g$\n")
sys.stdout.write("     ################################<-g$\n")
sys.stdout.write("     ################################<-g0\n")
sys.stdout.write("     ^^^^^\n")
sys.stdout.write("     |||||\n")
sys.stdout.write("     ggggg\n")
sys.stdout.write("     00000\n")
sys.stdout.write("     54321\n")

sys.stdout.write("\n")

sys.stdout.write("   lllllllll\n   ^^^^^^^^^\n   |||||||||I\n")
for n in range(1024):
 if n < 10:
  if bool(((b[n])/32)%2):
   sys.stdout.write("s->B")
  else:
   sys.stdout.write("s->b")
 else:
  if bool(((b[n])/32)%2):
   sys.stdout.write("   B")
  else:
   sys.stdout.write("   b")
 if bool(((b[n])/64)%2):
  sys.stdout.write("B")
 else:
  sys.stdout.write("b")
 if bool(((b[n])/128)%2):
  sys.stdout.write("B")
 else:
  sys.stdout.write("b")
 if bool(((g[n])/32)%2):
  sys.stdout.write("B")
 else:
  sys.stdout.write("b")
 if bool(((g[n])/64)%2):
  sys.stdout.write("B")
 else:
  sys.stdout.write("b")
 if bool(((g[n])/128)%2):
  sys.stdout.write("B")
 else:
  sys.stdout.write("b")
 if bool(((r[n])/32)%2):
  sys.stdout.write("B")
 else:
  sys.stdout.write("b")
 if bool(((r[n])/64)%2):
  sys.stdout.write("B")
 else:
  sys.stdout.write("b")
 if bool(((r[n])/128)%2):
  sys.stdout.write("B\n")
 else:
  sys.stdout.write("b\n")

sys.stdout.write("\n")

sys.stdout.write("1r---g11\n")

sys.stdout.write("\n")

sys.stdout.write("11g-]c]c]c]c]c]c]c]c]c]c\n")
sys.stdout.write("     | | | | | | | | | |\n")
sys.stdout.write("     g g g g g g g g g g\n")
sys.stdout.write("     0 0 0 0 0 0 0 0 0 1\n")
sys.stdout.write("     1 2 3 4 5 6 7 8 9 0\n")
sys.stdout.write("\n")
sys.stdout.write("    $$$$$$$$0\n    ggggggggg\n    |||||||||\n10g>i########\n09g>#########\n08g>#########\n07g>#########\n06g>#########\n05g>#########\n04g>#########\n03g>#########\n02g>#########\n01g>#########\n")
