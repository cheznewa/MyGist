import random
import sys
random.seed(sys.argv[1])
note = sys.stdin.read()
while True:
 maj = random.randint(1,16)
 n = random.randint(16,64)
 while n:
  noj = random.randint(1,16)
  k = float((maj*(1/8.0))+((1/16.0)*noj))
  j = 0
  while j < len(note):
   sys.stdout.write(note[int(j)])
   j = k+j
  n=n-1