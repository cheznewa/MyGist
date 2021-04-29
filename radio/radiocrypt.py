import sys
import random
seed = sys.argv[1]
mode = sys.argv[2]
random.seed(seed)
while True:
 o = sys.stdin.read(2)
 i = random.randint(3,268433)
 r = ord(o[1])*256 + ord(o[0])
 if mode == "enc":
  r = (r + i) % 65536
 if mode == "dec":
  r = (r - i) % 65536
 sys.stdout.write("%s%s" %(chr(r % 256),chr(r / 256)))