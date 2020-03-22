import sys
url = str(sys.argv[1])
mode = str(sys.argv[2])
colorpourcent = float(sys.argv[3])
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

def cond(bool):
 if bool:
  return "Oui"
 else:
  return "Non"

syster_table = (ord(reshash[0])%2)+1

import time
hashtwo = hashlib.sha256()
hashtwo.update("%s%s" %(reshash,int(time.time()/86400)))
hashday = hashtwo.digest()

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

 if ord(reshash[1]) >= 100:
  cryptage = "Transcode"

 if ord(reshash[1]) < 100:
  cryptage = "Nagravision Syster"

 if ord(reshash[1]) < 50:
  cryptage = "VideoCrypt"

 if ord(reshash[1]) < 5:
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

if mode == "syster":
 cryptage = "Nagravision Syster"

if mode == "discret11":
 cryptage = "Discret 11"

if mode == "videocrypt":
 cryptage = "VideoCrypt"

if mode == "transcode":
 cryptage = "Transcode"

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

# Begin XXX
if mode == "normal":
 if bool(re.search("redtraffic",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  color = "NTSC"
  videocrypt_stricte = False

 if bool(re.search("www\.ast\.tv",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  color = "PAL"
  videocrypt_stricte = False

 if bool(re.search("jasminchannel",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  color = "PAL"
  videocrypt_stricte = False

 if bool(re.search("a2\.skynets\.tv",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  color = "PAL"
  videocrypt_stricte = False

 if bool(re.search("psrv\.io",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  color = "PAL"
  videocrypt_stricte = False

 if bool(re.search("iptvipaccess\.es",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  color = "PAL"
  videocrypt_stricte = False

 if bool(re.search("wer5tuuh\.russtv\.net",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  color = "SECAM"
  videocrypt_stricte = False

 if bool(re.search("nruxmzi\.ojswi5dsmftgm2ldfz4hs6q\.cmle\.ru",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  color = "SECAM"
  videocrypt_stricte = False
# End XXX

if colorpourcent < float(ord(reshash[5])/256.0):
 color = "Aucun"

radio = (((ord(reshash[6])*256)+ord(reshash[7]))*100)
radioend = radio + 100

print("Votre IPTV Chiffrer Par CryptImage Pour ::: " + url)
print("System De Chiffrement :: "+cryptage)
print("Plage Radio Utiliser :: %s-%s" %(str(radio),str(radioend)))
print("Modem Couleur :: "+color)
if cryptage == "VideoCrypt":
 print("Point De Coupe :: "+str(videocrypt_begin)+"-"+str(videocrypt_end))
 print("Mode Stricte :: "+cond(videocrypt_stricte))
 print("Tatouage Dans La Ligne 576 :: "+cond(tag_enable))
 print("Son Traiter :: "+cond(soundcrypt_enable))
 print("Pour Le Dechiffrer Vous Devrait Jouer A Geometry Dash Et Avoir :: "+str(int(stars*10))+" Etoile")
if cryptage == "Nagravision Syster":
 print("Table Primaire :: "+str(syster_table))
 print("Demi-Ligne :: "+cond(syster_demi))
 print("Tatouage Dans La Ligne 288 :: "+cond(tag_enable))
 print("Son Traiter :: "+cond(soundcrypt_enable))
 print("Pour Le Dechiffrer Vous Devrait Jouer A Geometry Dash Et Avoir :: "+str(int(stars*5))+" Etoile")
if cryptage == "Discret 11":
 sys.stdout.write("Mot De 16 Bit :: ")
 sys.stdout.write("%s\n" %(word))
 sys.stdout.write("Multicode :: ")
 for n in range(10):
  sys.stdout.write("%s" %(level[n]))
 sys.stdout.write("\n")
 print("Son Traiter :: "+cond(soundcrypt_enable))
 print("Pour Le Dechiffrer Vous Devrait Jouer A Geometry Dash Et Avoir :: "+str(int(stars*3))+" Etoile")
if cryptage == "Transcode":
 print("Donc Toute Est En Claire !")
