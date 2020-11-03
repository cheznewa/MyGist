# Try ::::::::: calc "3^1000" | tr -d "    " | python2 truncat.py 200 | python2 truncat_pow.py 200 3 4000
import sys
text = sys.stdin.read()
begin,lengn,end = text.split(" ")
la = int(sys.argv[1])
bas = int(sys.argv[2])
exp = int(sys.argv[3])
n = int(lengn[4:-4])
n=n+(la*2)
m=0
while m <= exp:
 a = len(begin)
 begin = str(bas*int(begin))
 end = str(bas*int(end))
 b = len(begin)
 n = n + (b-a)
 begin = begin[:la]
 end = end[-la:]
 m = m+1
sys.stdout.write(begin)
sys.stdout.write(" ...[%s]... " %(n-(la*2)))
sys.stdout.write(end)