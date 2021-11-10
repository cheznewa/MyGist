import sys
import re
thinlevel = 1/float(pow(int(sys.argv[1]),2))
circ = sys.stdin.read()
c = re.sub("\"[^\"]*\"","",circ)
price = 0
price += c.count("v") + c.count("w")
price += c.count("^") + c.count("m")
price += c.count("<") + c.count("[")
price += c.count(">") + c.count("]")
pricefinal = (thinlevel*price)/(1+((c.count("I")+c.count("i"))/2))
sys.stdout.write("%s\n" %(pricefinal))