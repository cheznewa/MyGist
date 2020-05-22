import sys
from base58 import b58decode,b58encode_int
o = sys.stdin.read()
a = ""
for n in o:
 a += str(b58encode_int(int(58*(ord(n)/256.0))))
sys.stdout.write(b58decode(a))