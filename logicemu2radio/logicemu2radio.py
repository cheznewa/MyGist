import sys
map = ["-","|","+",".","/","\\","x","g","a","A","o","O","e","E","h","H","f","F","s","S","l","r","R","p","P","c","C","y","j","k","t","d","q","Q","b","B","M","U","^",">","v","<","m","]","w","[","V","W","X","Y","#","=","i","I","T","D","(",")","n","u",",","%","&","*","z","Z","?","N","J","K","0","1","2","3","4","5","6","7","8","9","$"," ","\n"] # A Copy From The Original Source
h = False
while True:
 o = sys.stdin.read(1)
 m = map.index(o)
 a = m / 10
 b = m % 10
 sys.stdout.write(chr(5+(b*10)+100))
 sys.stdout.write(chr(5+(a*10)+100))