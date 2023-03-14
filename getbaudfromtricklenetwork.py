import sys
alice=sys.argv[1]
bob  =sys.argv[2]
vv=[400,600,555,255,123,765,386,1000,547,664,22,457,100,6543,458,333,666,999,556]
mm=max(len(alice),len(bob))
baud=0
for n in range(mm):
 baud = baud + vv[(ord(alice[n%len(alice)])+ord(bob[n%len(bob)]))%len(vv)]

final = (baud%57550)+50

sys.stdout.write("%s\n" %(final))
