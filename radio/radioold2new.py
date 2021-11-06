import sys
from base58 import b58decode_int
from struct import pack
for o in sys.stdin:
 sys.stdout.write("%s" %(pack("I",b58decode_int(o))))