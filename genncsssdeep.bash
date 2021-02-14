# Pour Générer Un Fichier SSDEEP Contient Touts Les NoCopyrightsounds Avec SongRec Afin D'Identifier Une Musique NCS
# Premier Argument Est La Sortie
# Usage Après Génération ::::::::::::::: songrec audio-file-to-fingerprint votreaudio | cut -d , -f 2 | base64 -d | ssdeep -m votressdeepgenerer.txt
# Requis ::::: SongRec et SSDeep
tmp=$(mktemp -d)
youtube-dl -o "$tmp/%(title)s.%(ext)s" -i https://soundcloud.com/nocopyrightsounds
for u in $tmp/*
do
songrec audio-file-to-fingerprint "$u" | cut -d , -f 2 | base64 -d > "$u.fingerprint"
done
ssdeep -b $tmp/*.fingerprint > "$1"
rm -r $tmp
