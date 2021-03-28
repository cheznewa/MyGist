from ppyssdeep import *
import random
import sys
numberwords = int(sys.argv[1])
limitewarning = int(sys.argv[2])
fs = open("/usr/share/dict/words","r")
instd = ssdeep_hash(sys.stdin.read())
words = fs.readlines()
g = numberwords
pharse = " "
while True:
 while bool(g):
  pharse = pharse + " " + random.choice(words)
  g = g - 1
 hash = ssdeep_hash(pharse)
 g = numberwords
 pharse = " "
 n = ssdeep_compare(instd,hash)
 if n >= limitewarning:
  sys.stdout.write("Warning! Except %s Purcento Is Copy!! Hello? Hello??\n" %(n))