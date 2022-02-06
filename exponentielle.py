import sys
base = int(sys.argv[1])
digits = int(sys.argv[2])
num = int(sys.argv[3])
div,mod = divmod(num,base)
j = div
ret = 0
while j:
 ret = (ret + pow(base,j,pow(10,digits))) % pow(10,digits)
 j=j-1
ret = (ret + (mod*pow(base,div))) % pow(10,digits)
sys.stdout.write("%s\n" %(ret))