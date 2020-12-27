import sys
import hashlib
hash = hashlib.sha256()
hash.update(sys.argv[1])
reshash = hash.digest()
player = ord(reshash[0])%99
ball = ord(reshash[1])%43
robot = ord(reshash[2])%26
ship = ord(reshash[3])%31
wave = ord(reshash[4])%35
spider = ord(reshash[5])%17
ufo = ord(reshash[6])%35
cola = ord(reshash[7])%41
colb = ord(reshash[8])%41
glow = int(ord(reshash[9]) > 164)
 
sys.stdout.write("https://gdbrowser.com/icon/icon?icon=%s&form=player&col1=%s&col2=%s&glow=%s\n" %(player+1,cola,colb,glow))
sys.stdout.write("https://gdbrowser.com/icon/icon?icon=%s&form=ship&col1=%s&col2=%s&glow=%s\n" %(ship+1,cola,colb,glow))
sys.stdout.write("https://gdbrowser.com/icon/icon?icon=%s&form=ball&col1=%s&col2=%s&glow=%s\n" %(ball+1,cola,colb,glow))
sys.stdout.write("https://gdbrowser.com/icon/icon?icon=%s&form=ufo&col1=%s&col2=%s&glow=%s\n" %(ufo+1,cola,colb,glow))
sys.stdout.write("https://gdbrowser.com/icon/icon?icon=%s&form=wave&col1=%s&col2=%s&glow=%s\n" %(wave+1,cola,colb,glow))
sys.stdout.write("https://gdbrowser.com/icon/icon?icon=%s&form=robot&col1=%s&col2=%s&glow=%s\n" %(robot+1,cola,colb,glow))
sys.stdout.write("https://gdbrowser.com/icon/icon?icon=%s&form=spider&col1=%s&col2=%s&glow=%s\n" %(spider+1,cola,colb,glow))