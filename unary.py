import sys
n = 0
for h in sys.stdin.read():
 if h == "1":
  n = n + 1
 if h == ".":
  n = pow(n,2)
 if h == "0":
  n = n - 1

sys.stdout.write(str(n))
