import sys
text = sys.stdin.read()
leng = len(text)
la = int(sys.argv[1])
sys.stdout.write(text[0:la])
sys.stdout.write(" ...[%s]... " %(leng-(la*2)))
sys.stdout.write(text[leng-la:leng])