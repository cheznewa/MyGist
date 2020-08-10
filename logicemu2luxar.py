import sys
import re
circ = sys.stdin.read()
def getmusicluxar(c):
 c = re.sub("\"[^\"]*\"","",c)
 icd = c.count("I")
 ic = c.count("i")
 logic = 0
 logic = logic + c.count("a")
 logic = logic + c.count("e")
 logic = logic + c.count("o")
 logicinv = 0
 logicinv = logicinv + c.count("A")
 logicinv = logicinv + c.count("E")
 logicinv = logicinv + c.count("O")
 switch = 0
 switch = switch + c.count("s")
 switch = switch + c.count("S")
 led = 0
 switch = switch + c.count("l")
 switch = switch + c.count("L")
 alu = c.count("U")
 term = c.count("T")
 matrix = c.count("D")
 quartz = c.count("t")
 pist = (alu + (logic - logicinv)) * (ic/(icd+1)) + (term%3) + switch + led + (matrix%7) + (quartz%5)
 return pist%16
luxartracks = ["Birth","First Step","Curiosity","Process","Will Free","Scar","Loneliness","Explorer","Chase","Revolution","Blooming","Torment","Awareness","Self-Confidence","Ambition","Responsability"]
get = getmusicluxar(circ)
print("La Musique Luxar Pour Ce Circuit Est ::::: " + luxartracks[get])
print("Piste Numero ::::::::: " + str(get+1))
