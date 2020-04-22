import sys
import hashlib
input = sys.stdin.read()
hash = hashlib.sha256()
hash.update(input)
atwork = int(hash.hexdigest(),16)
opened = True
difficulty = int(sys.argv[1])
fill = pow(2,256)-1
mask = fill/difficulty
nonce = 0 + difficulty
while opened:
 output = pow(atwork,nonce,fill)
 if output < mask:
  sys.stdout.write("Trouver A La Profondeur ::::: %s\n" %(nonce))
  opened = False
 nonce = nonce + 1