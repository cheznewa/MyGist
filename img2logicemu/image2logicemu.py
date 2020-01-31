import sys
from PIL import Image
img = Image.open(sys.argv[1])
imga = img.resize((32,32))
r = list(bytearray(imga.getdata(0)))
g = list(bytearray(imga.getdata(1)))
b = list(bytearray(imga.getdata(2)))
sys.stdout.write("10g->D###############################<--g0\n")
sys.stdout.write("09g->################################<-c\n")
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
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################\n")
sys.stdout.write("     ################################<-g11\n")
sys.stdout.write("     ################################<-g12\n")
sys.stdout.write("     ################################<-g13\n")
sys.stdout.write("     ################################<-g14\n")
sys.stdout.write("     ^^^^^\n")
sys.stdout.write("     |||||\n")
sys.stdout.write("     ggggg\n")
sys.stdout.write("     00000\n")
sys.stdout.write("     54321\n")

sys.stdout.write("\n")

sys.stdout.write("   llll\n   ^^^^\n   ||||I\n")
for n in range(1024):
 if n < 10:
  if int(r[n]) >= int(sys.argv[2]):
   sys.stdout.write("s->B")
  else:
   sys.stdout.write("s->b")
 else:
  if int(b[n]) >= int(sys.argv[2]):
   sys.stdout.write("   B")
  else:
   sys.stdout.write("   b")
 if int(g[n]) >= int(sys.argv[2]):
  sys.stdout.write("B")
 else:
  sys.stdout.write("b")
 if int(r[n]) >= int(sys.argv[2]):
  sys.stdout.write("B")
 else:
  sys.stdout.write("b")
 if ((int(b[n])+int(g[n])+int(r[n]))/3) >= int(sys.argv[3]):
  sys.stdout.write("B\n")
 else:
  sys.stdout.write("b\n")

sys.stdout.write("\n")

sys.stdout.write("1r---g0\n")

sys.stdout.write("\n")

sys.stdout.write("0g-]c]c]c]c]c]c]c]c]c]c\n")
sys.stdout.write("    | | | | | | | | | |\n")
sys.stdout.write("    g g g g g g g g g g\n")
sys.stdout.write("    0 0 0 0 0 0 0 0 0 1\n")
sys.stdout.write("    1 2 3 4 5 6 7 8 9 0\n")
sys.stdout.write("\n")
sys.stdout.write("    1111\n    1234\n    gggg\n    ||||\n10g>####\n09g>#i##\n08g>####\n07g>####\n06g>####\n05g>####\n04g>####\n03g>####\n02g>####\n01g>####\n")
