import sys
from base58 import b58encode,b58decode_int
i = sys.stdin.read()
for n in b58encode(i):
 sys.stdout.write(chr(1+int(256*(b58decode_int(n)/58.0))))