import sys
url = str(sys.argv[1])
mode = str(sys.argv[2])
payment = str(sys.argv[3])
colorpourcent = float(sys.argv[4])
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
videocrypt_begin_one = vcbegin[ord(end[4]) % 127]
videocrypt_end_one = vcend[ord(end[7]) % 126]
videocrypt_begin_two = vcbegin[ord(end[5]) % 127]
videocrypt_end_two = vcend[ord(end[8]) % 126]
videocrypt_begin_three = vcbegin[ord(end[6]) % 127]
videocrypt_end_three = vcend[ord(end[9]) % 126]

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

retardone = ((float((ord(reshash[24]) *256)+(ord(hashday[25])))/65536)*2.5)+0.5
retardtwo = ((float((ord(reshash[26]) *256)+(ord(hashday[27])))/65536)*3.0)+2.0

level = []
for n in range(11,21):
 level.append((ord(hashday[n])%6)+1)

syster_demi = bool(ord(end[0])%2)

stars = (1.0/((1+ord(reshash[10]))/256.0))+1.0

coin = (1.0/((1+ord(reshash[22]))/256.0))+1.0

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

if mode == "onion":
 cryptage = "VideoCrypt"
 soundcrypt_enable = False
 videocrypt_stricte = False
 tag_enable = False


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
  coin = 100
  color = "NTSC"
  videocrypt_stricte = False
  tag_enable = False
  
  if mode == "normal":
 if bool(re.search("adultiptv",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  coin = 100
  color = "NIIR"
  videocrypt_stricte = False
  tag_enable = False

 if bool(re.search("www\.ast\.tv",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  coin = 100
  color = "PAL"
  videocrypt_stricte = False
  tag_enable = False

 if bool(re.search("jasminchannel",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  coin = 100
  color = "PAL"
  videocrypt_stricte = False
  tag_enable = False

 if bool(re.search("a2\.skynets\.tv",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  coin = 100
  color = "PAL"
  videocrypt_stricte = False
  tag_enable = False

 if bool(re.search("psrv\.io",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  coin = 100
  color = "PAL"
  videocrypt_stricte = False
  tag_enable = False

 if bool(re.search("iptvipaccess\.es",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  coin = 100
  color = "PAL"
  videocrypt_stricte = False
  tag_enable = False

 if bool(re.search("wer5tuuh\.russtv\.net",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  coin = 100
  color = "SECAM"
  videocrypt_stricte = False
  tag_enable = False

 if bool(re.search("nruxmzi\.ojswi5dsmftgm2ldfz4hs6q\.cmle\.ru",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  coin = 100
  color = "SECAM"
  videocrypt_stricte = False
  tag_enable = False

 if bool(re.search("cdn1\.ibizastream\.biz",url)):
  cryptage = "VideoCrypt"
  videocrypt_begin = 1
  videocrypt_end = 255
  soundcrypt_enable = True
  stars = 500
  coin = 100
  color = "MAC"
  videocrypt_stricte = False
  tag_enable = False
# End XXX

if colorpourcent < float(ord(reshash[5])/256.0):
 color = "Aucun"

if ord(reshash[18]) > 173:
 planif = range(0,20)
 planiftcbegin = planif[ord(reshash[16])%19]
 planif = range(1,6)
 planiftcend = planif[ord(reshash[17])%5]
 planiftcend = planiftcend + planiftcbegin
 planifbeginend = str(planiftcbegin) + ":00 - " + str(planiftcend) + ":00"
else:
 planiftcbegin = 0
 planiftcend = 0
 planifbeginend = "Aucun"

typetext = bool(ord(reshash[9]) > 40)

if typetext:
 ttv = "A"
else:
 ttv = "B"

radio = (((ord(reshash[8])*65536)+(ord(reshash[6])*256)+ord(reshash[7]))*10000)
radioend = radio + 10000

print("Votre IPTV Chiffrer Par CryptImage Pour ::: " + url)
print("System De Chiffrement :: "+cryptage)
print("Plage Radio Utiliser :: %s-%s" %(str(radio),str(radioend)))
print("Modem Couleur :: "+color)
if cryptage == "VideoCrypt":
 print("Point De Coupe :: "+str(videocrypt_begin)+"-"+str(videocrypt_end))
 print("Mode Stricte :: "+cond(videocrypt_stricte))
 print("Tatouage Dans La Ligne 576 :: "+cond(tag_enable))
 print("Son Traiter :: "+cond(soundcrypt_enable))
 print("Horaire De Transcode :: " + planifbeginend)
 if payment == "dash":
  print("Pour Le Dechiffrer Vous Devrait Jouer A Geometry Dash Et Avoir :: "+str(int(stars*10)-((planiftcbegin-planiftcend)/10))+" Etoile")
 if payment == "coin":
  print("Pour Le Dechiffrer Vous Devrait Payer :: "+str(int(coin*20)-((planiftcbegin-planiftcend)/20))+" Piece/Foitierre")
 if mode == "onion":
  print("Vous Etes En Routage Onion, Apres Vous Avez Encore 3 Chiffrement Supplementaire Par Relais :::: ")
  print("Point De Coupe Relais 1 :: "+str(videocrypt_begin_one)+"-"+str(videocrypt_end_one))
  print("Point De Coupe Relais 2 :: "+str(videocrypt_begin_two)+"-"+str(videocrypt_end_two))
  print("Point De Coupe Relais 3 :: "+str(videocrypt_begin_three)+"-"+str(videocrypt_end_three))
if cryptage == "Nagravision Syster":
 print("Table Primaire :: "+str(syster_table))
 print("Demi-Ligne :: "+cond(syster_demi))
 print("Tatouage Dans La Ligne 288 :: "+cond(tag_enable))
 print("Son Traiter :: "+cond(soundcrypt_enable))
 print("Horaire De Transcode :: " + planifbeginend)
 if payment == "dash":
  print("Pour Le Dechiffrer Vous Devrait Jouer A Geometry Dash Et Avoir :: "+str(int(stars*5)-((planiftcbegin-planiftcend)/5))+" Etoile")
 if payment == "coin":
  print("Pour Le Dechiffrer Vous Devrait Payer :: "+str(int(coin*10)-((planiftcbegin-planiftcend)/10))+" Piece/Foitierre")
if cryptage == "Discret 11":
 sys.stdout.write("Mot De 16 Bit :: ")
 sys.stdout.write("%s\n" %(word))
 sys.stdout.write("Multicode :: ")
 for n in range(10):
  sys.stdout.write("%s" %(level[n]))
 sys.stdout.write("\n")
 print("Retard 1 :: "+str(retardone))
 print("Retard 2 :: "+str(retardtwo))
 print("Son Traiter :: "+cond(soundcrypt_enable))
 print("Horaire De Transcode :: " + planifbeginend)
 if payment == "dash":
  print("Pour Le Dechiffrer Vous Devrait Jouer A Geometry Dash Et Avoir :: "+str(int(stars*3)-((planiftcbegin-planiftcend)/3))+" Etoile")
 if payment == "coin":
  print("Pour Le Dechiffrer Vous Devrait Payer :: "+str(int(coin*5)-((planiftcbegin-planiftcend)/5))+" Piece/Foitierre")
if cryptage == "Transcode":
 print("Donc Toute Est En Claire !")
print("Variante Du Teletext :: " + ttv)
