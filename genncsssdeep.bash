# Pour Générer Un Fichier SSDEEP Contient Touts Les NoCopyrightsounds En Pitch Afin De Identifier Une Musique NCS
# Premier Argument Est La Sortie
# Usage Après Génération ::::::::::::::: aubio pitch mamusique.mp3 | cut -d "	" -f 2 | cur -d "." -f 1 | ssdeep -m votressdeepgenerer.txt
# Requis ::::: Aubio et SSDeep
tmp=$(mktemp -d)
youtube-dl -o "$tmp/%(title)s.%(ext)s" -i https://soundcloud.com/nocopyrightsounds
for u in $tmp/*
do
aubio pitch "$u" | cut -d "	" -f 2 | cur -d "." -f 1 > "$u.pitch"
done
ssdeep -b $tmp/*.pitch > "$1"
rm -r $tmp
