import sys
start = int(sys.argv[1])+1
ended = int(sys.argv[2])+1
if start == 1:
 sys.stdout.write("4.")
 start = 2
rng = range(start,ended)
for i in rng:
 s = str(i*i)
 n = 0
 for u in range(len(s)):
  n = n + int(s[u])
 n = (10-(n%10))%10
 sys.stdout.write("%s" %(n))
sys.stdout.write("\n")