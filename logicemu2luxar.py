import sys
import re
circ = sys.stdin.read()
def getmusicluxar(c):
 c = re.sub("\"[^\"]*\"","",c)
 indown = c.count("v") - c.count("w")
 inup = c.count("^") - c.count("m")
 inleft = c.count("<") - c.count("[")
 inright = c.count(">") - c.count("]")
 return (((inleft/3)%2)*8)+(((inup/3)%2)*4)+(((inright/3)%2)*2)+((indown/3)%2)
luxartracks = ["Birth","First Step","Curiosity","Process","Free Will","Scar","Loneliness","Explorer","Chase","Revolution","Blooming","Torment","Awareness","Self-Confidence","Ambition","Responsability"]
get = getmusicluxar(circ)
sys.stdout.write("%s - %s" %(str(get+1),luxartracks[get]))
