import sys
n = 0
p = 0
for h in sys.stdin.read():
 if h == "1":
  n = n + 1
  if p > 0:
   n = n + pow(int(sys.argv[1]),p)
   p = 0
 if h == ".":
  p = p + 1

sys.stdout.write(str(n))
