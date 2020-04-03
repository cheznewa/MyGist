import sys
n = 0
for h in sys.stdin.read():
 if h == "1":
  n = n + 1
 if h == ".":
  n = n * int(sys.argv[1])

sys.stdout.write(str(n))
