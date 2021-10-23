import sys
o = sys.stdin.read()
s = 0
f = 0
for n in range(999):
 for i in o:
  s = (s+ord(i)+n) %999
 if s == 666:
  sys.stdout.write("Beast Number Found For %s Sum\n" %(n))
  f = f+1
 s = 0
for n in range(999):
 for i in o:
  s = (s+pow(ord(i),n,999))%999
 if s == 666:
  sys.stdout.write("Beast Number Found For %s Power\n" %(n))
  f = f+1
 s = 0
for n in range(999):
 for i in o:
  s = (s+pow(n,ord(i),999))%999
 if s == 666:
  sys.stdout.write("Beast Number Found For %s Expo\n" %(n))
  f = f+1
 s = 0

sys.stdout.write("Found The Beast Number :: %s Times\n" %(f))