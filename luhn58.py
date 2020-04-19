import base58
import sys
n = 0
s = 0
for g in sys.stdin.read():
 if bool(n % 2):
  l = 2 * base58.b58decode_int(g)
  if l > 57:
   l = l - 57
  s = s + l
 else:
  s = s + base58.b58decode_int(g)
 n = n + 1
 sys.stdout.write(g)

sys.stdout.write(str(base58.b58encode_int(s % 58)))