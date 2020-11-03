# Try ::::::::: calc "1000!" | tr -d "    " | python2 truncat.py 200 | python2 truncat_fact.py 200 1000 30000
import sys
text = sys.stdin.read()
begin,lengn,end = text.split(" ")
la = int(sys.argv[1])
fr = int(sys.argv[2])
to = int(sys.argv[3])
n = int(lengn[4:-4])
n=n+(la*2)
for t in range(fr,to):
 a = len(begin)
 begin = str((t+1)*int(begin))
 b = len(begin)
 n = n + (b-a)
 begin = begin[:la]
sys.stdout.write(begin)
sys.stdout.write(" ...[%s]... " %(n-(la*2)))
sys.stdout.write(text[-la:])