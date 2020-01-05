import sys
min = int(sys.argv[1])
max = int(sys.argv[2])
for o in sys.stdin:
 if int(o) >= min and int(o) < max:
  sys.stdout.write(chr(int((256.0*(int(o)-min)/(float(max)-float(min))))))