# Please Use pdftoroff ::::::::::::: pdftoroff -f your.pdf | python2 fontstats.py
# from https://github.com/sgerwk/pdftoroff
import sys
nbarray = 5000
fontid = [""] * nbarray
fontn  = [0]  * nbarray
t = 0
p = 0
while True:
 o = sys.stdin.read(1)
 if "\\" == o:
  if "[" == sys.stdin.read(1):
   f = ""
   i = True
   while i:
    s = sys.stdin.read(1)
    if "]" == s:
     i = False
     if f in fontid:
      p = fontid.index(f)
     else:
      fontid[t] = f
      p = t
      t = t + 1
    f = f + s
 if o:
  fontn[p] = fontn[p] + 1
 else:
  break
for n in range(t):
 sys.stdout.write(fontid[n])
 sys.stdout.write(" : ")
 sys.stdout.write(str(fontn[n]))
 sys.stdout.write("\n")
