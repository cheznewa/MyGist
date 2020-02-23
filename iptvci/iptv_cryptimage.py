import sys
url = str(sys.argv[1])
mode = str(sys.argv[2])
ip = str(sys.argv[3])
param = str(sys.argv[4])
import hashlib
import re
syster_table = 1
tag_enable = False
soundcrypt_enable = False
hash = hashlib.sha256()
hash.update(url)
reshash = hash.digest()
hash.update(reshash)
end = hash.digest()
vcbegin = range(1,129)
vcend = range(129,256)
videocrypt_begin = vcbegin[ord(reshash[0]) % 127]
videocrypt_end = vcend[ord(end[0]) % 126]

ipsplit = ip.split(".")
ipraw = chr(int(ipsplit[0]))+chr(int(ipsplit[1]))+chr(int(ipsplit[2]))+chr(int(ipsplit[3]))

def cond(bool):
 if bool:
  return "Oui"
 else:
  return "Non"

syster_table = (ord(reshash[0])%2)+1

import time
hashtwo = hashlib.sha256()
hashtwo.update("%s%s%s" %(reshash,int(time.time()/86400),ipraw))
hashday = hashtwo.digest()

fs = open(param,"w")

from random import seed,randint
seed("%s%s%s" %(reshash,hashday,ipraw))

word = ((((ord(hashday[0]) *256)+(ord(hashday[1]))))%65504)+32

level = []
for n in range(11,21):
 level.append((ord(hashday[n])%6)+1)

syster_demi = bool(ord(end[0])%2)

stars = (1.0/((1+ord(reshash[10]))/256.0))+1.0

videocrypt_stricte = bool(ord(end[1])%2)

if ord(end[2]) > 251:
 tag_enable = True

if mode == "normal":

 if ord(reshash[1]) <= 130:
  cryptage = "Transcode"

 if ord(reshash[1]) > 130:
  cryptage = "Nagravision Syster"

 if ord(reshash[1]) > 186:
  cryptage = "VideoCrypt"

 if ord(reshash[1]) > 250:
  cryptage = "Discret 11"

if mode == "noclear":

 if ord(reshash[1]) <= 50:
  cryptage = "Nagravision Syster"

 if ord(reshash[1]) > 50:
  cryptage = "VideoCrypt"

 if ord(reshash[1]) > 125:
  cryptage = "Discret 11"

 if ord(reshash[1]) > 130:
  cryptage = "Nagravision Syster"

 if ord(reshash[1]) > 186:
  cryptage = "VideoCrypt"

 if ord(reshash[1]) > 250:
  cryptage = "Discret 11"

# Begin XXX
if mode == "normal":
 if bool(re.search("redtraffic",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500

 if bool(re.search("www\.ast\.tv",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500

 if bool(re.search("jasminchannel",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
# End XXX

if mode == "syster":
 cryptage = "Nagravision Syster"

if mode == "discret11":
 cryptage = "Discret 11"

if mode == "videocrypt":
 cryptage = "VideoCrypt"

if cryptage == "VideoCrypt":
 if ord(reshash[3]) < 10:
  soundcrypt_enable = True

if cryptage == "Nagravision Syster":
 if ord(reshash[3]) > 10:
  soundcrypt_enable = True

if cryptage == "Discret 11":
 if ord(reshash[3]) > 20:
  soundcrypt_enable = True

if ord(reshash[2]) <= 220:
 color = "PAL"

if ord(reshash[2]) > 220:
 color = "NTSC"

if ord(reshash[2]) > 240:
 color = "SECAM"

if ord(reshash[2]) > 250:
 color = "NIIR"

if ord(reshash[2]) == 255:
 color = "MAC"

if bool(re.search("\.fr",url)):
  color = "SECAM"

if bool(re.search("\.ru",url)):
  color = "SECAM"

if bool(re.search("\.bg",url)):
  color = "SECAM"

if bool(re.search("nknews\.org",url)):
  color = "SECAM A"

if bool(re.search("\.be",url)):
  color = "SECAM"

if bool(re.search("international",url)):
  color = "MAC"

if bool(re.search("internacional",url)):
  color = "MAC"
  
if bool(re.search("tntendirect\.com/",url)):
  color = "SECAM"

if color == "SECAM":
 if ord(reshash[4]) > 220:
  color = "SECAM III"
 if ord(reshash[4]) > 230:
  color = "SECAM II"
 if ord(reshash[4]) > 240:
  color = "SECAM I"
 if ord(reshash[4]) > 245:
  color = "SECAM M"
 if ord(reshash[4]) > 250:
  color = "SECAM N"
 if ord(reshash[4]) == 255:
  color = "SECAM A"

if color == "PAL":
 if ord(reshash[4]) > 235:
  color = "PAL M"
 if ord(reshash[4]) > 250:
  color = "PAL N"

if color == "NIIR":
 if ord(reshash[4]) > 235:
  color = "NIIR M"
 if ord(reshash[4]) > 250:
  color = "NIIR N"

if color == "NTSC":
 if ord(reshash[4]) > 200:
  color = "NTSC N"
 if ord(reshash[4]) > 210:
  color = "NTSC I"
 if ord(reshash[4]) == 255:
  color = "NTSC A"

print("Votre IPTV Chiffrer Par CryptImage Pour ::: " + url)
print("System De Chiffrement :: "+cryptage)
print("Modem Couleur :: "+color)
if cryptage == "VideoCrypt":
 for n in range(86400*25):
  p = randint(1,1677216)
  fs.write("%s;%s;%s\n" %(p,videocrypt_begin,videocrypt_end))
 print("Point De Coupe :: "+str(videocrypt_begin)+"-"+str(videocrypt_end))
 print("Mode Stricte :: "+cond(videocrypt_stricte))
 print("Tatouage Dans La Ligne 576 :: "+cond(tag_enable))
 print("Son Traiter :: "+cond(soundcrypt_enable))
 print("Pour Le Dechiffrer Vous Devrait Jouer A Geometry Dash Et Avoir :: "+str(int(stars*10))+" Etoile")
if cryptage == "Nagravision Syster":
 for n in range(86400*25):
  aa = randint(0,255)
  ba = (randint(0,127)*2)+1
  if syster_demi:
   ab = randint(0,255)
   bb = (randint(0,127)*2)+1
  else:
   ab = aa
   bb = ba
  fs.write("frames %s;%s;%s;%s;%s;%s\n" %(n+1,syster_table,aa,ba,ab,bb))
 print("Table Primaire :: "+str(syster_table))
 print("Demi-Ligne :: "+cond(syster_demi))
 print("Tatouage Dans La Ligne 288 :: "+cond(tag_enable))
 print("Son Traiter :: "+cond(soundcrypt_enable))
 print("Pour Le Dechiffrer Vous Devrait Jouer A Geometry Dash Et Avoir :: "+str(int(stars*5))+" Etoile")
if cryptage == "Discret 11":
 fs.write("Mot De 16 Bit :: "+str(word)+"\n")
 fs.write("Multicode :: ")
 for n in range(10):
  fs.write("%s" %(level[n]))
 fs.write("\n")
 fs.close()
 print("Son Traiter :: "+cond(soundcrypt_enable))
 print("Pour Le Dechiffrer Vous Devrait Jouer A Geometry Dash Et Avoir :: "+str(int(stars*3))+" Etoile")
if cryptage == "Transcode":
 print("Donc Toute Est En Claire !")
