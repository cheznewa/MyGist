import sys
from random import sample,randint
nand = int(sys.argv[1])
regs = int(sys.argv[2])
inpu = int(sys.argv[3])
outp = int(sys.argv[4])
gate = sys.argv[5]

for n in range(inpu):
 sys.stdout.write("%sg-s\n@\n" %(n))
for n in range(inpu,+inpu+outp):
 sys.stdout.write("l<g%s\n@\n" %(n))

h = nand
m = regs

while nand:
 sys.stdout.write("#-g%s\n#<g%s\n%s<g%s\n@\n" %(nand+inpu,randint(0,h+m+inpu+outp),gate,randint(0,h+m+inpu+outp)))
 nand=nand-1

while regs:
 sys.stdout.write("#-g%s\nd<g%s\nc<g%s\n@\n" %(h+regs+inpu,randint(0,h+m+inpu+outp),randint(0,h+m+inpu+outp)))
 regs=regs-1